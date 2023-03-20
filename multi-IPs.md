场景一：单张网卡配置多个IP

场景二：多张网卡配置多个IP



### 场景一：单张网卡配置多个IP

按照以下的方式，创建多个预留公网IP地址

<img width="940" alt="767e900dbcb8327e9170dc7ae58eb94" src="https://user-images.githubusercontent.com/4653664/226293414-dbd35987-b83c-4661-8c45-07e338eb7733.png">


将创建的预留公网IP分配给虚拟机的`Primary VNIC`（`Compute Instances->Instance details->Attached VNICs`）

<img width="849" alt="1679303196279" src="https://user-images.githubusercontent.com/4653664/226293813-75403665-425f-4671-92e2-adcce7e5811c.png">

最终的效果类似如下：

<img width="878" alt="1679303326001" src="https://user-images.githubusercontent.com/4653664/226294300-1f5bd58d-dc39-464f-aeef-a3de682daaa2.png">

在操作系统层面配置使用这两个IP地址，注意这里添加的私有IP地址。

```
[root@test001 ~]# ip addr add 10.0.0.54/24 dev ens3 label ens3:0
[root@test001 ~]# ip addr add 10.0.0.252/24 dev ens3 label ens3:1
```

> 注意，以上是临时配置，在虚拟机重启后将失效，持久化配置参考如下：

```
#/etc/sysconfig/network-scripts/ifcfg-ens3:0

DEVICE="ens3:0"
BOOTPROTO=static
IPADDR=10.0.0.54
NETMASK=255.255.255.0
ONBOOT=yes
```


验证是否添加成功

```
[root@test001 ~]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 02:00:17:03:da:6a brd ff:ff:ff:ff:ff:ff
    altname enp0s3
    inet 10.0.0.108/24 brd 10.0.0.255 scope global dynamic ens3
       valid_lft 85857sec preferred_lft 85857sec
    inet 10.0.0.54/24 scope global secondary ens3:0
       valid_lft forever preferred_lft forever
    inet 10.0.0.252/24 scope global secondary ens3:1
       valid_lft forever preferred_lft forever
    inet6 fe80::17ff:fe03:da6a/64 scope link
       valid_lft forever preferred_lft forever
```

测试添加的新公网IP是否可以Ping通

```
[root@test001 ~]# ping -c 3 138.3.221.181
PING 138.3.221.181 (138.3.221.181) 56(84) bytes of data.
64 bytes from 138.3.221.181: icmp_seq=1 ttl=63 time=0.305 ms
64 bytes from 138.3.221.181: icmp_seq=2 ttl=63 time=0.216 ms
64 bytes from 138.3.221.181: icmp_seq=3 ttl=63 time=0.223 ms

--- 138.3.221.181 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2068ms
rtt min/avg/max/mdev = 0.216/0.248/0.305/0.040 ms
[root@test001 ~]#
[root@test001 ~]#
[root@test001 ~]# ping -c 3 138.3.222.233
PING 138.3.222.233 (138.3.222.233) 56(84) bytes of data.
64 bytes from 138.3.222.233: icmp_seq=1 ttl=63 time=0.210 ms
64 bytes from 138.3.222.233: icmp_seq=2 ttl=63 time=0.220 ms
64 bytes from 138.3.222.233: icmp_seq=3 ttl=63 time=0.253 ms

--- 138.3.222.233 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2063ms
rtt min/avg/max/mdev = 0.210/0.227/0.253/0.025 ms

```

### 场景二：多张网卡配置多个IP

这里仅演示如何配置带有公网IP的第二张网卡。

<img width="930" alt="1679303717599" src="https://user-images.githubusercontent.com/4653664/226295787-d99cdd9b-ebe1-4971-8382-16ab8558d728.png">






