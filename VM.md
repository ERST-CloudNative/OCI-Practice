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

### 场景-02：VM+数据盘(iSCSI)，制作镜像，然后基于镜像创建新的VM

相关步骤与场景-01类似，这里部分内容简述

1. 创建虚拟机test-003
2. 创建块存储卷test-003
3. 将块存储卷test-003以iSCSI方式挂载虚拟机test-003

<img width="960" alt="1688122774765" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1c7ca7ae-ba2e-46a0-84f7-4df6f5d4c77b">

获取挂载命令行信息

<img width="947" alt="1688122839191" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3d5c6176-ed7f-49a0-b244-8a395a8b8f68">
<img width="486" alt="1688122888963" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f85c9082-56bf-4b80-95b6-6aa3b111e93d">


4. 访问虚拟机

```
[root@test-003 ~]# # 执行上一步获取的挂载命令
[root@test-003 ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0 46.6G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
sdb                  8:16   0   50G  0 disk
[root@test-003 ~]# mkmkdir -p /opt/test
-bash: mkmkdir: command not found
[root@test-003 ~]# mkdir -p /opt/test
[root@test-003 ~]# mkfs.xfs /dev/sdb
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
[root@test-003 ~]# blkid /dev/sdb
/dev/sdb: UUID="8c70f6b4-1f2a-463b-a4b8-a52ddafead8a" BLOCK_SIZE="4096" TYPE="xfs"
[root@test-003 ~]# vi /etc/fstab
[root@test-003 ~]# echo "UUID=8c70f6b4-1f2a-463b-a4b8-a52ddafead8a  /opt/test            xfs    defaults,noatime,_netdev        0 0" >> /etc/fstab
[root@test-003 ~]# mount -a
[root@test-003 ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  1.8G     0  1.8G   0% /dev
tmpfs                      tmpfs     1.8G     0  1.8G   0% /dev/shm
tmpfs                      tmpfs     1.8G  8.7M  1.8G   1% /run
tmpfs                      tmpfs     1.8G     0  1.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  8.7G   27G  25% /
/dev/mapper/ocivolume-oled xfs        10G  105M  9.9G   2% /var/oled
/dev/sda2                  xfs      1014M  334M  681M  33% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs     362M     0  362M   0% /run/user/0
tmpfs                      tmpfs     362M     0  362M   0% /run/user/988
tmpfs                      tmpfs     362M     0  362M   0% /run/user/1000
/dev/sdb                   xfs        50G  389M   50G   1% /opt/test
[root@test-003 ~]# echo 1234 >> /opt/test/test.txt
[root@test-003 ~]# cat /opt/test/test.txt
1234
```

6. 制作镜像test-003
7. 使用镜像test-003创建虚拟机test-003-image-vm
8. 克隆test-003块存储
9. 挂载test-003-clone块存储
10. 访问虚拟机test-003-image-vm
<img width="878" alt="1688124085734" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5c394593-18ac-474a-9e71-a6c2e14507d6">

```
[root@test-003-image-vm ~]# lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                  8:0    0 46.6G  0 disk
├─sda1               8:1    0  100M  0 part /boot/efi
├─sda2               8:2    0    1G  0 part /boot
└─sda3               8:3    0 45.5G  0 part
  ├─ocivolume-root 252:0    0 35.5G  0 lvm  /
  └─ocivolume-oled 252:1    0   10G  0 lvm  /var/oled
sdb                  8:16   0   50G  0 disk /opt/test

[root@test-003-image-vm ~]# df -hT
Filesystem                 Type      Size  Used Avail Use% Mounted on
devtmpfs                   devtmpfs  1.8G     0  1.8G   0% /dev
tmpfs                      tmpfs     1.8G     0  1.8G   0% /dev/shm
tmpfs                      tmpfs     1.8G   17M  1.8G   1% /run
tmpfs                      tmpfs     1.8G     0  1.8G   0% /sys/fs/cgroup
/dev/mapper/ocivolume-root xfs        36G  8.7G   27G  25% /
/dev/mapper/ocivolume-oled xfs        10G  108M  9.9G   2% /var/oled
/dev/sda2                  xfs      1014M  334M  681M  33% /boot
/dev/sda1                  vfat      100M  5.1M   95M   6% /boot/efi
tmpfs                      tmpfs     362M     0  362M   0% /run/user/0
tmpfs                      tmpfs     362M     0  362M   0% /run/user/988
tmpfs                      tmpfs     362M     0  362M   0% /run/user/1000
/dev/sdb                   xfs        50G  389M   50G   1% /opt/test


[root@test-003-image-vm ~]# cat /opt/test/test.txt
1234

```


为了能够让虚拟机自动挂载iSCSI卷，需要配置Oracle Cloud Agent的权限

获取区间OCID

<img width="422" alt="1688121127413" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/98398b72-e0c5-49d1-9254-1d54f03679ad">

<img width="711" alt="1688121187198" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/7664e3f4-5b7c-41b8-b173-e1faab7cd6e7">

获取租户OCID

<img width="954" alt="1688121621038" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b384cf1e-8906-4ad0-a6ac-60d1e3a22e9b">
<img width="837" alt="1688121693780" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/dc06370a-3aa5-4508-9ba8-ee6ba8e52ec0">


创建动态组
 
![Uploading 1688121779256.png…]()

```
ANY {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaazclvs3334e3g2fkfcrqiih7l7nrzoii7tl62hquoy5t4dp25j5ba'}
```
> 需要将instance.compartment.id的值修改为上一步获取的区间ID

<img width="957" alt="1688120842869" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ac14f4d6-3d84-419c-84b6-4667df4920e9">
<img width="953" alt="1688121318184" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/cd14480f-0c08-4ce3-9040-58f38d1b5de7">


创建权限策略

<img width="868" alt="1688121383570" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/9230444f-542c-4a78-9f44-d3b0459b395f">

<img width="877" alt="1688121446310" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/0511b90b-1c08-4b76-988e-74c70f6c1563">

<img width="754" alt="1688122028300" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d8f7e0d7-03b6-458e-ba66-67adef75354d">

创建虚拟机时主要勾选

<img width="681" alt="1688123608982" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/517b30f2-f085-4cc1-a7c4-30c200e330b0">

等待Block Volume Management插件running

<img width="951" alt="1688123926124" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5be4dde7-a735-471a-929d-f3b93ff5446f">


