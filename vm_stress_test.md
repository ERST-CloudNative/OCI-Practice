## 虚拟机压测


### CPU/MEM使用率

在特定负载运行的场景下，查看服务器端CPU/MEM的使用率.


服务器端（待测试服务器）

```
[root@test-0x ~]# systemctl stop firewalld
[root@test-0x ~]# systemctl disable firewalld
[root@test-0x ~]# echo ulimit -n 655350 >> /etc/profile
[root@test-0x ~]# source /etc/profile
[root@test-0x ~]# yum install -y nginx
[root@test-0x ~]# systemctl start nginx
```

客户端

```
[root@test-0x ~]# wget https://github.com/fortio/fortio/releases/download/v1.54.0/fortio-1.54.0-1.x86_64.rpm
[root@test-0x ~]# yum install -y ./fortio-1.54.0-1.x86_64.rpm
[root@test-0x ~]# systemctl stop firewalld
[root@test-0x ~]# systemctl disable firewalld
[root@test-0x ~]# echo ulimit -n 655350 >> /etc/profile
[root@test-0x ~]# source /etc/profile
[root@test-0x ~]# fortio server
```

访问fortio UI界面

```
http://YOUR_NLB_PUBLIC_IP:8080/fortio/
```

模拟压力测试场景

<img width="949" alt="1694504731290" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d4d3a18c-8cf3-4637-9398-c6f41f4ba2c6">


<img width="950" alt="1694504687857" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c893d859-4476-40f3-891a-59557d2cbb92">

查看CPU/MEM使用率均值

<img width="831" alt="1694504770067" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/81539046-6558-47e3-96c3-ba72ee8b15f2">


### 网络带宽

```
[root@test-002-2o8g ~]# iperf3 -s -f M
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
Accepted connection from 152.67.194.186, port 39058
[  5] local 10.0.0.252 port 5201 connected to 152.67.194.186 port 39060
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec   331 MBytes   331 MBytes/sec
[  5]   1.00-2.00   sec   220 MBytes   220 MBytes/sec
[  5]   2.00-3.00   sec   263 MBytes   263 MBytes/sec
[  5]   3.00-4.00   sec   200 MBytes   200 MBytes/sec
[  5]   4.00-5.00   sec   280 MBytes   280 MBytes/sec
[  5]   5.00-6.00   sec   195 MBytes   195 MBytes/sec
[  5]   6.00-7.00   sec   272 MBytes   272 MBytes/sec
[  5]   7.00-8.00   sec   212 MBytes   212 MBytes/sec
[  5]   8.00-9.00   sec   252 MBytes   252 MBytes/sec
[  5]   9.00-10.00  sec   231 MBytes   231 MBytes/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.04  sec  2.40 GBytes   244 MBytes/sec                  receiver
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------

```


```
[root@test-001-2o8g ~]# yum install -y iperf3
[root@test-001-2o8g ~]# iperf3 -c 158.180.69.215 -f M
Connecting to host 158.180.69.215, port 5201
[  5] local 10.0.0.38 port 39060 connected to 158.180.69.215 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   334 MBytes   334 MBytes/sec  705    227 KBytes
[  5]   1.00-2.00   sec   239 MBytes   239 MBytes/sec  772   2.39 MBytes
[  5]   2.00-3.00   sec   244 MBytes   244 MBytes/sec  1052    192 KBytes
[  5]   3.00-4.00   sec   220 MBytes   220 MBytes/sec  747   1.83 MBytes
[  5]   4.00-5.00   sec   262 MBytes   262 MBytes/sec  1076    201 KBytes
[  5]   5.00-6.00   sec   200 MBytes   200 MBytes/sec  759    419 KBytes
[  5]   6.00-7.00   sec   281 MBytes   281 MBytes/sec  888   1.40 MBytes
[  5]   7.00-8.00   sec   195 MBytes   195 MBytes/sec  937    218 KBytes
[  5]   8.00-9.00   sec   271 MBytes   271 MBytes/sec  770   3.16 MBytes
[  5]   9.00-10.00  sec   211 MBytes   211 MBytes/sec  1073    201 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.40 GBytes   246 MBytes/sec  8779             sender
[  5]   0.00-10.04  sec  2.40 GBytes   244 MBytes/sec                  receiver

iperf Done.
```


