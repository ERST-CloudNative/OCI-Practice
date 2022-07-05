



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





![image](https://user-images.githubusercontent.com/4653664/177259569-cd426dbf-e579-428c-84c5-7edefca005b4.png)

