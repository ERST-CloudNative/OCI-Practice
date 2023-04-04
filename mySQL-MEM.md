
## MySQL Enterprise Monitor部署

#### 1. 环境配置

```
systemctl stop firewalld;systemctl disable firewalld
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf install docker-ce -y
systemctl enable docker --now

```

#### 2. 部署MEM

```
docker run -d --name mysql8 --net=host -e MYSQL_ROOT_PASSWORD=OCI_test_123 mysql:8.0.32-oracle
docker run -d --name mme-ui --net=host b43646/mem:v1.0
```

#### 3. 访问MEM

默认地址为https://【Your VM Public IP】:18443/



![image](https://user-images.githubusercontent.com/4653664/229786158-8cdca5b8-9302-40b9-843d-e30af1607729.png)
