### 挂载数据盘

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


