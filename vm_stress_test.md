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


```


