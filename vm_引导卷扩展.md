## 虚拟机引导卷扩展


在虚拟机创建时，默认引导卷存储50GB,但有时候需要更大的卷存储空间，这里可以在创建时直接调整（如100GB），但调整后，文件系统看只有50GB，以下部分主要介绍如何调整到目标存储空间，如100GB.


```
# 查看文件系统容量，当前为50GB
[root@redis01 ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  3.7G     0  3.7G   0% /dev
tmpfs                      tmpfs     3.8G     0  3.8G   0% /dev/shm
tmpfs                      tmpfs     3.8G  8.7M  3.8G   1% /run
tmpfs                      tmpfs     3.8G     0  3.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  8.9G   27G  25% /
/dev/mapper/ocivolume-oled xfs        10G  106M  9.9G   2% /var/oled
/dev/sda2                  xfs      1014M  354M  661M  35% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs     764M     0  764M   0% /run/user/0
tmpfs                      tmpfs     764M     0  764M   0% /run/user/987
tmpfs                      tmpfs     764M     0  764M   0% /run/user/1000
[root@redis01 ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0  100G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled

# 安装相关工具
[root@redis01 ~]# yum install -y cloud-utils-growpart gdisk

# 扩展分区
[root@redis01 ~]# growpart /dev/sda 3
CHANGED: partition=3 start=2304000 old: size=95371264 end=97675263 new: size=207411167 end=209715166

# 验证分区sda3已经完成扩展
[root@redis01 ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0  100G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 98.9G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled

# 查看LVM相关配置
[root@redis01 ~]# vgs
  VG        #PV #LV #SN Attr   VSize   VFree
  ocivolume   1   2   0 wz--n- <98.90g <53.43g
[root@redis01 ~]# lvs
  LV   VG        Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  oled ocivolume -wi-ao---- 10.00g
  root ocivolume -wi-ao---- 35.47g
[root@redis01 ~]# pvs
  PV         VG        Fmt  Attr PSize   PFree
  /dev/sda3  ocivolume lvm2 a--  <98.90g <53.43g


# 扩展逻辑卷
[root@redis01 ~]# lvextend -l +100%FREE  /dev/ocivolume/root
  Size of logical volume ocivolume/root changed from 35.47 GiB (9081 extents) to <88.90 GiB (22758 extents).
  Logical volume ocivolume/root successfully resized.
[root@redis01 ~]# lvs
  LV   VG        Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  oled ocivolume -wi-ao----  10.00g
  root ocivolume -wi-ao---- <88.90g

# 扩展文件系统大小
[root@redis01 ~]# xfs_growfs /dev/ocivolume/root
meta-data=/dev/mapper/ocivolume-root isize=512    agcount=4, agsize=2324736 blks
         =                       sectsz=4096  attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=0 inobtcount=0
data     =                       bsize=4096   blocks=9298944, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=4540, version=2
         =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 9298944 to 23304192

# 验证文件系统大小
[root@redis01 ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  3.7G     0  3.7G   0% /dev
tmpfs                      tmpfs     3.8G     0  3.8G   0% /dev/shm
tmpfs                      tmpfs     3.8G  8.7M  3.8G   1% /run
tmpfs                      tmpfs     3.8G     0  3.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        89G   11G   79G  12% /
/dev/mapper/ocivolume-oled xfs        10G  121M  9.9G   2% /var/oled
/dev/sda2                  xfs      1014M  354M  661M  35% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs     764M     0  764M   0% /run/user/0
tmpfs                      tmpfs     764M     0  764M   0% /run/user/987
tmpfs                      tmpfs     764M     0  764M   0% /run/user/1000


```
