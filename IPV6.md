
#### OCI中如何使用IPv6

1. 在已经创建好的VCN中创建新的Subnet，并且使能IPV6地址网段

![image](https://user-images.githubusercontent.com/4653664/216945976-ce52cbe0-177a-4ac1-a64f-e5b167f4f98d.png)


2. 在新建的Subent中创建虚拟机

![image](https://user-images.githubusercontent.com/4653664/216946492-9d9f0bf2-72fb-4218-98b0-6ee40758e526.png)

3. 在虚拟机主网卡上分配IPV6的地址

![image](https://user-images.githubusercontent.com/4653664/216946739-e91f379c-85ee-4435-9bea-924f663b179d.png)

4. 为IPV6网段添加路由表

![image](https://user-images.githubusercontent.com/4653664/216946989-2623df63-0542-40f1-8402-e726098bc019.png)

5. 配置Security List中安全规则

![image](https://user-images.githubusercontent.com/4653664/216947148-24f577ec-ea5d-4b2e-81f6-0d3a63bae6e6.png)


6. 登录虚拟机，配置使用IPV6地址

```
[root@instance-20230206-1643 ~]# dhclient -6
dhclient(40930) is already running - exiting.

This version of ISC DHCP is based on the release available
on ftp.isc.org. Features have been added and other changes
have been made to the base software release in order to make
it work better with this distribution.

Please report issues with this software via:
https://bugzilla.oracle.com/

exiting.
```

7. 验证IPV6地址可用性

```
[root@instance-20230206-1643 ~]# ping6 2603:c021:8010:3111:3e6e:f953:2536:9766
PING 2603:c021:8010:3111:3e6e:f953:2536:9766(2603:c021:8010:3111:3e6e:f953:2536:9766) 56 data bytes
64 bytes from 2603:c021:8010:3111:3e6e:f953:2536:9766: icmp_seq=1 ttl=64 time=0.053 ms
64 bytes from 2603:c021:8010:3111:3e6e:f953:2536:9766: icmp_seq=2 ttl=64 time=0.040 ms
64 bytes from 2603:c021:8010:3111:3e6e:f953:2536:9766: icmp_seq=3 ttl=64 time=0.040 ms
64 bytes from 2603:c021:8010:3111:3e6e:f953:2536:9766: icmp_seq=4 ttl=64 time=0.041 ms
^C
--- 2603:c021:8010:3111:3e6e:f953:2536:9766 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3092ms
rtt min/avg/max/mdev = 0.040/0.043/0.053/0.008 ms


[root@instance-20230206-1643 ~]# curl -I http://[2603:c021:8010:3111:3e6e:f953:2536:9766]/
HTTP/1.1 200 OK
Server: nginx/1.14.1
Date: Mon, 06 Feb 2023 10:24:54 GMT
Content-Type: text/html
Content-Length: 3949
Last-Modified: Thu, 19 Sep 2019 18:38:36 GMT
Connection: keep-alive
ETag: "5d83cb2c-f6d"
Accept-Ranges: bytes
```




