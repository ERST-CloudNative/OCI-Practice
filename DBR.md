
VCN10: 10.10.0.0/16

VCN20: 10.20.0.0/16


创建VCN

![image](https://user-images.githubusercontent.com/4653664/179775047-58553ce0-d098-479b-82db-0fb443bf9ad4.png)

![image](https://user-images.githubusercontent.com/4653664/179775448-94cd0f54-1a88-4fd4-8947-3d6c3b6184b0.png)

创建DBR

![image](https://user-images.githubusercontent.com/4653664/179775345-f9df62e4-00ba-4e73-a480-8b1a147a8702.png)


在VCN20中完成以下操作

(1)添加更新路由表

![image](https://user-images.githubusercontent.com/4653664/179775787-ad556c98-22aa-4531-aeea-9665dc192a20.png)


(2)添加更新安全列表

![image](https://user-images.githubusercontent.com/4653664/179775989-8e292310-9540-4680-9964-2974edf1ac46.png)

![image](https://user-images.githubusercontent.com/4653664/179776380-b0a42bb5-78cb-437f-ae67-15a781464562.png)

在VCN10中完成类似操作

![image](https://user-images.githubusercontent.com/4653664/179777014-9f8d1aed-123d-4011-b6c8-8f696572cab3.png)

![image](https://user-images.githubusercontent.com/4653664/179777356-f38ad965-ae0e-4959-9885-35322825afbd.png)

![image](https://user-images.githubusercontent.com/4653664/179777554-3e4b2ad6-eecc-495e-914a-54548b928796.png)

验证网络连通性

```
[root@vcn10 ~]# ping -c 3 10.20.0.110
PING 10.20.0.110 (10.20.0.110) 56(84) bytes of data.
64 bytes from 10.20.0.110: icmp_seq=1 ttl=63 time=0.352 ms
64 bytes from 10.20.0.110: icmp_seq=2 ttl=63 time=0.402 ms
64 bytes from 10.20.0.110: icmp_seq=3 ttl=63 time=0.389 ms

--- 10.20.0.110 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2036ms
rtt min/avg/max/mdev = 0.352/0.381/0.402/0.021 ms
[root@vcn10 ~]#
[root@vcn10 ~]#
[root@vcn10 ~]# ping -c 3 140.83.57.200
PING 140.83.57.200 (140.83.57.200) 56(84) bytes of data.
64 bytes from 140.83.57.200: icmp_seq=1 ttl=63 time=0.454 ms
64 bytes from 140.83.57.200: icmp_seq=2 ttl=63 time=0.393 ms
64 bytes from 140.83.57.200: icmp_seq=3 ttl=63 time=0.370 ms

--- 140.83.57.200 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2034ms
rtt min/avg/max/mdev = 0.370/0.405/0.454/0.042 ms
```
