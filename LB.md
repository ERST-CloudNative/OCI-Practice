
### L7 负载均衡实验


安装nginx
```
[root@host-10-0-0-179 ~]# yum install -y nginx
```

开放80端口

```
[root@host-10-0-0-179 ~]# firewall-cmd --add-port=80/tcp --permanent
success
[root@host-10-0-0-179 ~]# firewall-cmd --reload
success
```
更新节点Nginx index页面信息

```
# vi /usr/share/nginx/html/index.html
       <h1>Welcome to <strong>nginx-001</strong> on Oracle Linux!</h1>
```
> 不同云主机，选择不同的NGINX-00x

启动NGINX服务

```
[root@host-10-0-0-179 ~]# systemctl start nginx
```

针对实例2，重复以上步骤.


![image](https://user-images.githubusercontent.com/4653664/177256946-5badb721-c89c-4d86-87ad-271fbd56b368.png)

创建L7 LB

![image](https://user-images.githubusercontent.com/4653664/177260018-55fe27ef-5a4f-4a7b-9d3b-1022c6a88c33.png)

![image](https://user-images.githubusercontent.com/4653664/177260036-23b08536-e332-413d-8da2-595ff62a1ddc.png)

![image](https://user-images.githubusercontent.com/4653664/177260070-cd018e53-f1cf-47e0-9135-4c74081c9117.png)

![image](https://user-images.githubusercontent.com/4653664/177260088-85638159-3bbb-403f-a86e-48343906cc0e.png)

![image](https://user-images.githubusercontent.com/4653664/177260105-5c719dad-2b0d-42b2-b7bd-8f194df16a9d.png)

![image](https://user-images.githubusercontent.com/4653664/177260120-2f9e3b8c-f738-42d7-8c0b-cb055891e881.png)

![image](https://user-images.githubusercontent.com/4653664/177260134-465016b4-035e-4252-9d3c-11cac1480bcc.png)


验证LB已经可以实现对后端NGINX服务的负载均衡

![image](https://user-images.githubusercontent.com/4653664/177260165-e15aaa81-64d6-4ffc-a154-47ecf018690f.png)

![image](https://user-images.githubusercontent.com/4653664/177260182-f4f05955-0380-4aa3-9952-b0cf48f7b8b5.png)


终止LB
![image](https://user-images.githubusercontent.com/4653664/177259840-09f4161f-4ed8-41c4-a381-a6247a604f08.png)

移除放开80端口的规则

![image](https://user-images.githubusercontent.com/4653664/177259569-cd426dbf-e579-428c-84c5-7edefca005b4.png)

