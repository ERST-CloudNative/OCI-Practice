### 纵向伸缩

##### 扩容CPU/MEM

```
[root@host-10-0-0-179 ~]# lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  2
Core(s) per socket:  1
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
BIOS Vendor ID:      QEMU
CPU family:          6
Model:               106
Model name:          Intel(R) Xeon(R) Platinum 8358 CPU @ 2.60GHz
BIOS Model name:     pc-i440fx-4.2
Stepping:            6
CPU MHz:             2593.984
BogoMIPS:            5187.96
Virtualization:      VT-x
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            4096K
L3 cache:            16384K
NUMA node0 CPU(s):   0,1
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves nt_good wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid md_clear arch_capabilities
[root@host-10-0-0-179 ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            680         361          50           1         268         212
Swap:          1360          18        1342
```
![image](https://user-images.githubusercontent.com/4653664/177253685-f01b24db-adfc-4e4d-8e9d-bfd2960338c8.png)

![image](https://user-images.githubusercontent.com/4653664/177254302-36022dbe-9eb1-417a-97a0-476857a0b6e7.png)

![image](https://user-images.githubusercontent.com/4653664/177254322-355c2390-e30c-4eda-9d8b-aa3f674f8a10.png)

实例更新后查看操作系统信息

```
[root@host-10-0-0-179 ~]# lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  2
Core(s) per socket:  2
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
BIOS Vendor ID:      QEMU
CPU family:          6
Model:               106
Model name:          Intel(R) Xeon(R) Platinum 8358 CPU @ 2.60GHz
BIOS Model name:     pc-i440fx-4.2
Stepping:            6
CPU MHz:             2593.986
BogoMIPS:            5187.97
Virtualization:      VT-x
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            4096K
L3 cache:            16384K
NUMA node0 CPU(s):   0-3
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves nt_good wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid md_clear arch_capabilities

[root@host-10-0-0-179 ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:           3635         366        2750           8         519        3032
Swap:          1360           0        1360

```

##### 缩容CPU/MEM

![image](https://user-images.githubusercontent.com/4653664/177254626-972ae554-ab1f-48bb-93a4-ab699d3d9aee.png)

![image](https://user-images.githubusercontent.com/4653664/177254681-6d28f042-5c81-4dbd-8e10-1257d894d2cc.png)

实例更新后查看操作系统信息

```
[root@host-10-0-0-179 ~]# lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  2
Core(s) per socket:  1
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
BIOS Vendor ID:      QEMU
CPU family:          6
Model:               106
Model name:          Intel(R) Xeon(R) Platinum 8358 CPU @ 2.60GHz
BIOS Model name:     pc-i440fx-4.2
Stepping:            6
CPU MHz:             2593.986
BogoMIPS:            5187.97
Virtualization:      VT-x
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            4096K
L3 cache:            16384K
NUMA node0 CPU(s):   0,1
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves nt_good wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid md_clear arch_capabilities
[root@host-10-0-0-179 ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            680         412          45           1         223         162
Swap:          1360          30        1330


```


### 数据盘挂载与卸载

##### 数据盘挂载

1. 创建数据盘

![image](https://user-images.githubusercontent.com/4653664/177243490-705ce274-c853-456e-9f3c-93e963c7155f.png)


2. 查看iSCSI连接信息

![image](https://user-images.githubusercontent.com/4653664/177243664-e9917baa-bdf9-46ac-8092-c76745c1c23f.png)


![image](https://user-images.githubusercontent.com/4653664/177243360-16848c32-1d17-48f7-ada5-e5d61268d42a.png)


3. 连接iSCSI存储

```
sudo iscsiadm -m node -o new -T iqn.2015-12.com.oracleiaas:ac526d34-86fc-4148-aafe-191c47c26c1a -p 169.254.2.2:3260
sudo iscsiadm -m node -o update -T iqn.2015-12.com.oracleiaas:ac526d34-86fc-4148-aafe-191c47c26c1a -n node.startup -v automatic
sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:ac526d34-86fc-4148-aafe-191c47c26c1a -p 169.254.2.2:3260 -l
```

验证块存储已经连接到目标主机
```
[root@bootstrap ~]# ls /dev/oracleoci/ -l
total 0
lrwxrwxrwx. 1 root root 6 Jul  5 03:00 oraclevda -> ../sda
lrwxrwxrwx. 1 root root 7 Jul  5 03:00 oraclevda1 -> ../sda1
lrwxrwxrwx. 1 root root 7 Jul  5 03:00 oraclevda2 -> ../sda2
lrwxrwxrwx. 1 root root 7 Jul  5 03:00 oraclevda3 -> ../sda3
lrwxrwxrwx. 1 root root 6 Jul  5 03:18 oraclevdb -> ../sdb
```

查看块存储详情，如存储空间

```
[root@bootstrap ~]# fdisk -l
GPT PMBR size mismatch (97677311 != 104857599) will be corrected by write.
The backup GPT table is not on the end of the device. This problem will be corrected by write.
Disk /dev/sda: 50 GiB, 53687091200 bytes, 104857600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes
Disklabel type: gpt
Disk identifier: F2AE61A1-DA96-4DB2-9DBC-B30652CE1420

Device       Start      End  Sectors  Size Type
/dev/sda1     2048   206847   204800  100M EFI System
/dev/sda2   206848  2303999  2097152    1G Linux filesystem
/dev/sda3  2304000 97675263 95371264 45.5G Linux LVM


Disk /dev/mapper/ocivolume-root: 35.5 GiB, 38088474624 bytes, 74391552 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes


Disk /dev/mapper/ocivolume-oled: 10 GiB, 10737418240 bytes, 20971520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes


Disk /dev/sdb: 50 GiB, 53687091200 bytes, 104857600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes
```

4. 块存储分区

分区

```
[root@bootstrap ~]# fdisk /dev/sdb

Welcome to fdisk (util-linux 2.32.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x970e85a5.

Command (m for help): p
Disk /dev/sdb: 50 GiB, 53687091200 bytes, 104857600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes
Disklabel type: dos
Disk identifier: 0x970e85a5

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1):
First sector (2048-104857599, default 2048):
Last sector, +sectors or +size{K,M,G,T,P} (2048-104857599, default 104857599):

Created a new partition 1 of type 'Linux' and of size 50 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

告知操作系统分区更新

```
[root@bootstrap ~]# partprobe /dev/sdb
```

查看分区是否完成

```
[root@bootstrap ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0   50G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
sdb                  8:16   0   50G  0 disk
└─sdb1               8:17   0   50G  0 part

[root@bootstrap ~]# ls /dev/sdb*
/dev/sdb  /dev/sdb1

```

5. 格式化分区

这里我们选择XFS作为目标块存储的文件系统

```
[root@bootstrap ~]# mkfs -t xfs /dev/sdb1
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=3276736 blks
         =                       sectsz=4096  attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1
data     =                       bsize=4096   blocks=13106944, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=6399, version=2
         =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```

获取设备ID,用于系统重启后自动挂载存储

```
[root@bootstrap ~]# blkid /dev/sdb1
/dev/sdb1: UUID="a6587cc9-4a95-413d-a63e-856b1559b1fa" BLOCK_SIZE="4096" TYPE="xfs" PARTUUID="970e85a5-01"
```

创建挂载点/opt/demo
```
[root@bootstrap ~]# mkdir /opt/demo
```

将挂载信息更新到/etc/fstab文件中

```
[root@bootstrap ~]# vi /etc/fstab
[root@bootstrap ~]# echo "UUID=a6587cc9-4a95-413d-a63e-856b1559b1fa /opt/demo            xfs     defaults        0 0" >> /etc/fstab
```

挂载
```
[root@bootstrap ~]# mount -a
```

6. 测试验证

验证挂载信息
```
[root@bootstrap ~]# mount | grep demo
/dev/sdb1 on /opt/demo type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)
[root@bootstrap ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  303M     0  303M   0% /dev
tmpfs                      tmpfs     342M     0  342M   0% /dev/shm
tmpfs                      tmpfs     342M  4.9M  337M   2% /run
tmpfs                      tmpfs     342M     0  342M   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  5.4G   31G  16% /
/dev/sda2                  xfs      1014M  314M  701M  31% /boot
/dev/mapper/ocivolume-oled xfs        10G  121M  9.9G   2% /var/oled
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs      69M     0   69M   0% /run/user/0
tmpfs                      tmpfs      69M     0   69M   0% /run/user/987
tmpfs                      tmpfs      69M     0   69M   0% /run/user/1000
/dev/sdb1                  xfs        50G  390M   50G   1% /opt/demo

```

验证是否可以正常读写
```
[root@bootstrap ~]# echo 123 > /opt/demo/demo.txt

[root@bootstrap ~]# cat /opt/demo/demo.txt
123
```

##### 数据盘卸载

1. 卸载挂载点

```
[root@bootstrap ~]# umount /opt/demo
```

注释掉之前加入/etc/fstab文件中的设备信息，避免再次启动时挂载失败

```
# /etc/fstab

# UUID=a6587cc9-4a95-413d-a63e-856b1559b1fa /opt/demo            xfs     defaults        0 0
```

2. 断开iSCSI连接

查看iSCSI命令和信息

![image](https://user-images.githubusercontent.com/4653664/177251735-5f9bc933-d5a9-4456-9f14-3faead250922.png)


断开连接
```
[root@bootstrap ~]# sudo iscsiadm -m node -T iqn.2015-12.com.oracleiaas:ac526d34-86fc-4148-aafe-191c47c26c1a -p 169.254.2.2:3260 -u
[root@bootstrap ~]# sudo iscsiadm -m node -o delete -T iqn.2015-12.com.oracleiaas:ac526d34-86fc-4148-aafe-191c47c26c1a -p 169.254.2.2:3260
```

3. 验证块设备已移除

```
[root@bootstrap ~]# ls /dev/oracleoci/ -l
total 0
lrwxrwxrwx. 1 root root 6 Jul  5 03:29 oraclevda -> ../sda
lrwxrwxrwx. 1 root root 7 Jul  5 03:29 oraclevda1 -> ../sda1
lrwxrwxrwx. 1 root root 7 Jul  5 03:29 oraclevda2 -> ../sda2
lrwxrwxrwx. 1 root root 7 Jul  5 03:29 oraclevda3 -> ../sda3
```

4. 分离块存储卷资源

![image](https://user-images.githubusercontent.com/4653664/177252403-3a9ced95-d3b5-4848-9a22-58e6b125231e.png)

5. 终止块存储资源

![image](https://user-images.githubusercontent.com/4653664/177252564-498d1d92-a481-4018-8505-4bb624b2dc61.png)

