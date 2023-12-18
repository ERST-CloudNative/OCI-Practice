## OKE网络规划与集群创建

### 1. 网络规划


```
OKE_POD_SUBNET_CIDR  10.0.0.0/18
OKE_NODE_SUBNET_CIDR  10.0.64.0/22
OKE_API_SUBNET_CIDR  10.0.68.0/22
OKE_SVCLB_SUBNET_CIDR 10.0.72.0/22
VM_SUBNET_01_CIDR 10.0.76.0/24
```

### 2. VCN配置

> 注意：以下子网配置，请按照上一步网络规划中的CIDR进行配置。

创建VCN

<img width="823" alt="1702886273132" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e1249d28-38d9-4252-b83d-69c4233a8ac9">

创建所需的子网

<img width="941" alt="1702886346244" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/68901fd6-281a-4447-8d02-bf2c8c3e182a">


其中，Security Lists可以新建或者使用默认的配置，这里选择默认配置

<img width="620" alt="1701693665280" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d435ec78-6d56-40ee-ab4a-504ba2c28d48">

配置默认的安全列表，这里添加两条安全规则：
1. 允许节点间通信
2. 允许访问master集群api端口

<img width="944" alt="1701693753666" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/03b32034-b179-4171-af24-0d8b51a561a6">


配置IGW和路由表

<img width="635" alt="1702879144875" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/0eba9a38-7a79-429c-b58f-b0424fb9cdb5">

在默认的路由表中添加一条路由规则

<img width="586" alt="1702879232118" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5688d0d2-86f9-4b25-afd0-b669168ecc60">

配置NAT网关和路由表

<img width="634" alt="1702885910789" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6ff48352-61c5-46fc-81a5-995a193325a6">

新建路由表，并添加NAT规则

<img width="579" alt="1702885969430" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/482cca1a-dd72-4067-bca0-b74c02066841">

<img width="517" alt="1702886012285" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/10a7db69-3623-42d7-bba7-0ec566a38d9a">



### 3. OKE集群创建

<img width="725" alt="1702886488062" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/05f8c43d-f585-433c-826e-9ebdd4f92a10">

<img width="825" alt="1702886542622" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e74c5a5f-1c38-413d-935b-8c39eeed71b9">

<img width="884" alt="1702886647911" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/45f8af71-b860-484e-ad7d-393c10c36fe2">

<img width="847" alt="1702886697977" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5782a622-353b-4894-b9d1-26470a62ddb8">

其中，节点个数和节点配置信息按需配置即可。

<img width="827" alt="1702886798269" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f5ed290a-5cf1-4192-af3b-7c967c7fbf4f">


引导卷扩容后，需要在操作系统层面做相应的操作，这里使用cloud init脚本完成

```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh
sudo -i
dd iflag=direct if=/dev/oracleoci/oraclevda of=/dev/null count=1
echo "1" | sudo tee /sys/class/block/`readlink /dev/oracleoci/oraclevda | cut -d'/' -f 2`/device/rescan
growpart /dev/sda 3
lvextend -l +100%FREE  /dev/ocivolume/root
xfs_growfs /dev/ocivolume/root
```

<img width="958" alt="1701694331319" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/87c5e5b5-152d-45d0-9c15-05e02b4052fe">

<img width="867" alt="1701694362814" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c29abd75-2bb1-482e-aaec-25a745306295">

<img width="960" alt="1701694399763" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/df7401e9-ff82-4a70-a6c8-293e0a98e16c">


### 4. OKE集群验证

1. 验证节点池全部就绪

<img width="950" alt="1701695427140" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ed58e790-ac6c-4cb2-b856-0b74c9cc3aff">

2. 验证节点存储扩容是否配置生效

<img width="766" alt="1701695486715" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/4940376c-89bb-4562-bc2b-f79c0bac8390">

3. 验证集群功能是否符合预期

这里集群创建了9个node节点，查看节点是否全部ready

```
longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl get nodes
NAME          STATUS   ROLES   AGE     VERSION
10.0.11.169   Ready    node    7m6s    v1.27.2
10.0.17.232   Ready    node    7m55s   v1.27.2
10.0.2.11     Ready    node    7m      v1.27.2
10.0.2.192    Ready    node    7m13s   v1.27.2
10.0.21.151   Ready    node    7m12s   v1.27.2
10.0.23.99    Ready    node    7m9s    v1.27.2
10.0.4.229    Ready    node    7m57s   v1.27.2
10.0.40.41    Ready    node    7m6s    v1.27.2
10.0.41.114   Ready    node    8m3s    v1.27.2
```

创建nginx测试用例，9个副本，确认所有副本都可以正常调度到每个节点

```
longfei_re@cloudshell:~ (ap-chuncheon-1)$ cat test.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 9
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl apply -f test.yaml 
longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl get pods -o wide
NAME                        READY   STATUS    RESTARTS   AGE    IP            NODE          NOMINATED NODE   READINESS GATES
my-nginx-57d84f57dc-7ld44   1/1     Running   0          106s   10.0.60.173   10.0.17.232   <none>           <none>
my-nginx-57d84f57dc-8rjzl   1/1     Running   0          107s   10.0.52.4     10.0.40.41    <none>           <none>
my-nginx-57d84f57dc-jprnf   1/1     Running   0          106s   10.0.5.41     10.0.2.11     <none>           <none>
my-nginx-57d84f57dc-mp2r9   1/1     Running   0          106s   10.0.37.193   10.0.4.229    <none>           <none>
my-nginx-57d84f57dc-pxjmq   1/1     Running   0          106s   10.0.14.234   10.0.23.99    <none>           <none>
my-nginx-57d84f57dc-rzj5g   1/1     Running   0          106s   10.0.9.113    10.0.2.192    <none>           <none>
my-nginx-57d84f57dc-sjqbj   1/1     Running   0          106s   10.0.12.236   10.0.21.151   <none>           <none>
my-nginx-57d84f57dc-wjkhr   1/1     Running   0          106s   10.0.60.145   10.0.41.114   <none>           <none>
my-nginx-57d84f57dc-wm6h4   1/1     Running   0          106s   10.0.11.24    10.0.11.169   <none>           <none>

```

### 5. OKE集群扩容验证

将节点池的节点数量扩容到10个节点

<img width="944" alt="1701695820807" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3e7fdfc5-5eaa-4030-8107-866166f88dcf">

验证节点创建成功

<img width="950" alt="1701696124739" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ef8646a8-37fe-414b-b338-36bfa56b3a91">

```
longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl get nodes
NAME          STATUS   ROLES   AGE    VERSION
10.0.11.169   Ready    node    14m    v1.27.2
10.0.17.232   Ready    node    15m    v1.27.2
10.0.2.11     Ready    node    14m    v1.27.2
10.0.2.192    Ready    node    15m    v1.27.2
10.0.21.151   Ready    node    15m    v1.27.2
10.0.23.99    Ready    node    15m    v1.27.2
10.0.27.101   Ready    node    2m7s   v1.27.2
10.0.4.229    Ready    node    15m    v1.27.2
10.0.40.41    Ready    node    14m    v1.27.2
10.0.41.114   Ready    node    15m    v1.27.2

longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl get nodes | grep 'Ready'| wc -l
10

# 验证外网通信
longfei_re@cloudshell:~ (ap-chuncheon-1)$ kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot
...                                                                                                                                                                                                                                                                                                                  
 tmp-shell  ~  ping google.com
PING google.com (142.250.199.110) 56(84) bytes of data.
64 bytes from nrt13s52-in-f14.1e100.net (142.250.199.110): icmp_seq=1 ttl=53 time=36.2 ms
64 bytes from nrt13s52-in-f14.1e100.net (142.250.199.110): icmp_seq=2 ttl=53 time=35.7 ms
64 bytes from nrt13s52-in-f14.1e100.net (142.250.199.110): icmp_seq=3 ttl=53 time=35.7 ms
64 bytes from nrt13s52-in-f14.1e100.net (142.250.199.110): icmp_seq=4 ttl=53 time=35.7 ms
```

