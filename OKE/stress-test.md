## 压测


### 1. 压测环境与架构

工具

```
压测工具：fortio v1.54.0
```

压测虚拟机配置

```
test-01: 8 OCPU/32GB
test-02: 8 OCPU/32GB
```

OKE集群的规模与配置

```
Kubernetes version: v1.26.2
Compute Nodes: 6
Compuye Node Resources: 8 OCPU/32GB/50GB
```

整体架构

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/dad387e9-e60e-4c7b-b7d1-dab3f18435e5)


### 2. 压测服务准备

Ingress Nginx部署

```
[root@demo ~]# wget https://raw.githubusercontent.com/ERST-CloudNative/OCI-Practice/main/OKE/ingress-nginx.yaml
# 删除其中的`loadBalancerIP: 158.101.71.121`,这里使用临时自动分配的公网IP地址
[root@demo ~]# vi ingress-nginx.yaml
[root@demo ~]# kc apply -f ingress-nginx.yaml
# 给6个计算节点打标签，确保ingress-nginx能够部署到对应的节点上
[root@demo ~]# kc label node YOUR_NODE_NAME ingress=nginx
# 按需扩容，也可以扩容到12个
[root@demo ~]# kc -n ingress-nginx scale deployment/ingress-nginx-controller --replicas=6
```
> 为了方便，可以将子网的securityList临时全部打开，测试完成后记得关闭。

部署应用

```
[root@demo ~]# cat nginx-test.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
[root@demo ~]# kc apply -f nginx-test.yaml
[root@demo ~]# kc get deployments
[root@demo ~]# kubectl expose deployment nginx-deployment
[root@demo ~]# kc get svc -A
[root@demo ~]# kubectl create ingress nginx-deployment --class=nginx --rule="loren.test.io/*=nginx-deployment:80"
[root@demo ~]# cat /etc/hosts
[root@demo ~]# echo "YOUR_NLB_PUBLIC_IP loren.test.io" >> /etc/hosts
[root@demo ~]# curl -I loren.test.io
HTTP/1.1 200 OK
Date: Fri, 16 Jun 2023 10:24:45 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 13 Jun 2023 17:34:28 GMT
ETag: "6488a8a4-267"
Accept-Ranges: bytes
```


### 2. 压测虚拟机的配置

```
[root@test-0x ~]# wget https://github.com/fortio/fortio/releases/download/v1.54.0/fortio-1.54.0-1.x86_64.rpm
[root@test-0x ~]# yum install -y ./fortio-1.54.0-1.x86_64.rpm
[root@test-0x ~]# systemctl stop firewalld
[root@test-0x ~]# systemctl disable firewalld
[root@test-0x ~]# echo ulimit -n 655350 >> /etc/profile
[root@test-0x ~]# source /etc/profile
[root@test-0x ~]# echo $YOUR_NLB_PUBLIC_IP loren.test.io >> /etc/hosts
```

### 3. 压测

分别启动test-01和test-02虚拟机上的压测服务

```
[root@test-0x ~]# fortio server
```

test-01压测配置与结果

<img width="587" alt="1686909670448" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f5844f59-5ec4-4fc6-8f69-180d727fc221">


<img width="949" alt="1686909508053" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f45d6ee2-51c0-4197-b14d-f61870deca02">

test-02压测配置与结果

<img width="945" alt="1686909697711" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6ea17cd4-8733-45ac-831c-49b8f345d99d">

<img width="953" alt="1686909569828" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e039d9e0-ea58-459a-94b3-11664ebef3b4">




