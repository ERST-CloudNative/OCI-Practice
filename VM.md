虚拟机使用场景

场景-1： VM+数据盘(半虚拟化)，制作镜像，然后基于镜像创建新的VM
场景-2： VM+数据盘(iSCSI)，制作镜像，然后基于镜像创建新的VM
场景-3： 基于VM实例的配置，构建VM的弹性伸缩池


### 场景-01：VM+数据盘(半虚拟化)，制作镜像，然后基于镜像创建新的VM

1. 创建虚拟机test-002

<img width="688" alt="1688118109518" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/748ceacf-54f8-4739-bbd5-c5dc4447c605">

2. 创建块存储test-002

<img width="949" alt="1688118176165" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6cb67121-2e51-4b26-bd79-d53c679d69f6">

3. 将块存储附加到虚拟机，并选择半虚拟化方式挂载

打开虚拟机详情页面，定位到左侧"Attached block volumes"

<img width="928" alt="1688118360698" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/31a6b33a-3956-44ff-9179-b968e88f29ea">

<img width="836" alt="1688118471752" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/aa322581-ff4e-4bda-a8c9-a0091dcb253d">

4. 通过SSH方式访问虚拟机，并将数据盘挂载到/opt/test目录

```
[opc@test-002 ~]$ sudo -i
[root@test-002 ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0 46.6G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
sdb                  8:16   0   50G  0 disk
[root@test-002 ~]# mkdir -p /opt/test
[root@test-002 ~]# mkfs.xfs /dev/sdb
meta-data=/dev/sdb               isize=512    agcount=4, agsize=3276800 blks
         =                       sectsz=4096  attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=0 inobtcount=0
data     =                       bsize=4096   blocks=13107200, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=25600, version=2
         =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
Discarding blocks...Done.
[root@test-002 ~]# blkid /dev/sdb
/dev/sdb: UUID="611cdb33-a922-4b6e-98de-288ba9d84b83" BLOCK_SIZE="4096" TYPE="xfs"
[root@test-002 ~]# echo "UUID=611cdb33-a922-4b6e-98de-288ba9d84b83 /opt/test            xfs     defaults        0 0" >> /etc/fstab
[root@test-002 ~]# mount -a
[root@test-002 ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  1.8G     0  1.8G   0% /dev
tmpfs                      tmpfs     1.8G     0  1.8G   0% /dev/shm
tmpfs                      tmpfs     1.8G  8.7M  1.8G   1% /run
tmpfs                      tmpfs     1.8G     0  1.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  8.3G   28G  24% /
/dev/mapper/ocivolume-oled xfs        10G  106M  9.9G   2% /var/oled
/dev/sda2                  xfs      1014M  334M  681M  33% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs     362M     0  362M   0% /run/user/0
tmpfs                      tmpfs     362M     0  362M   0% /run/user/988
tmpfs                      tmpfs     362M     0  362M   0% /run/user/1000
/dev/sdb                   xfs        50G  389M   50G   1% /opt/test
[root@test-002 ~]# cd /opt/test/
[root@test-002 test]# echo 123 >> test.txt
[root@test-002 test]# cat test.txt
123
```

5. 制作test-002虚拟机镜像

<img width="691" alt="1688118570595" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/62200fff-6aba-468e-be52-d1718f02bae1">

<img width="870" alt="1688118644613" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/57cfbf5f-d061-4642-a726-d09626ba1f20">

制作完成后，可以在OCI console界面上查看到新建的虚拟机镜像。

<img width="757" alt="1688118705658" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f386a4fb-40c2-4956-9374-b9dc99149abe">

6. 基于test-002虚拟机镜像创建新的虚拟机test-002-image-vm

这个过程与基于centos官方镜像创建虚拟机过程基本相同，但镜像部分需要选择我们定制的test-002镜像
<img width="612" alt="1688118813849" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8d5da640-f97a-4aed-9e44-998ee55eb693">

<img width="946" alt="1688118909433" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e3d38877-b2d0-4e5b-bb68-375310de8e4e">

7. 克隆test-002块存储

打开test-002块存储页面，选择“块存储卷克隆”

<img width="902" alt="1688119078761" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d02f0ee4-3fbe-464b-9370-f4b05ac713c7">

<img width="959" alt="1688119120356" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b5d078a0-2cfc-4035-86df-193af680b364">

8. 将克隆的块存储test-002-clone挂载到新建的虚拟机test-002-image-vm

<img width="958" alt="1688119311239" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/bb9a1b54-cbfd-4ac8-a898-a6059d6e3693">

9. 访问虚拟机test-002-image-vm

验证克隆的数据盘是否可以正常挂载，并验证数据的完整性

```
# 默认制作的
[root@test-002-image-vm ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  1.8G     0  1.8G   0% /dev
tmpfs                      tmpfs     1.8G     0  1.8G   0% /dev/shm
tmpfs                      tmpfs     1.8G   17M  1.8G   1% /run
tmpfs                      tmpfs     1.8G     0  1.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  8.3G   28G  24% /
/dev/sda2                  xfs      1014M  334M  681M  33% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
/dev/mapper/ocivolume-oled xfs        10G  107M  9.9G   2% /var/oled
tmpfs                      tmpfs     362M     0  362M   0% /run/user/988
tmpfs                      tmpfs     362M     0  362M   0% /run/user/0
tmpfs                      tmpfs     362M     0  362M   0% /run/user/1000

[root@test-002-image-vm ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0 46.6G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
[root@test-002-image-vm ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0 46.6G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
sdb                  8:16   0   50G  0 disk /opt/test

[root@test-002-image-vm ~]# blkid /dev/sdb
/dev/sdb: UUID="611cdb33-a922-4b6e-98de-288ba9d84b83" BLOCK_SIZE="4096" TYPE="xfs"


[root@test-002-image-vm ~]# echo "UUID=611cdb33-a922-4b6e-98de-288ba9d84b83 /opt/test            xfs     defaults        0 0" >> /etc/fstab

[root@test-002-image-vm ~]# mount -a

[root@test-002-image-vm ~]# ls /opt/test/
test.txt
[root@test-002-image-vm ~]# cat /opt/test/test.txt
123
```






