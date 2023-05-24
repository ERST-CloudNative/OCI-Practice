## OKE与LB的集成实践

OKE与LB的集成主要包含两种类型：
- L7 LB
- L4 NLB

这里仅涉及L7 LB

### 1. 通过OCI LB访问Nginx

配置文件

```
[root@loren lb]# cat nginx_lb.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
  labels:
    app: nginx
spec:
  replicas: 3
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
---
apiVersion: v1
kind: Service
metadata:
  name: my-nginx-svc
  labels:
    app: nginx
  annotations:
    oci.oraclecloud.com/load-balancer-type: "lb"
spec:
  type: LoadBalancer
  ports:
  - port: 80
  selector:
    app: nginx

```

创建Nginx LB

```
[root@loren lb]# kubectl apply -f nginx_lb.yaml
```

查看状态，可以看到`service/my-nginx-svc`已经有外部的公网IP

```
[root@loren lb]# kc get all
NAME                            READY   STATUS    RESTARTS   AGE
pod/my-nginx-6b7f675859-d7b6x   1/1     Running   0          29s
pod/my-nginx-6b7f675859-t8vjz   1/1     Running   0          29s
pod/my-nginx-6b7f675859-zxzrs   1/1     Running   0          30s

NAME                   TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)             AGE
service/kubernetes     ClusterIP      10.96.0.1     <none>            443/TCP,12250/TCP   90m
service/my-nginx-svc   LoadBalancer   10.96.45.84   141.147.167.193   80:32755/TCP        30s

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/my-nginx   3/3     3            3           30s

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/my-nginx-6b7f675859   3         3         3       30s

```

验证服务可以从公网访问

```
[root@loren lb]# curl -I 141.147.167.193
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 09:36:02 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

```

环境清理

```
[root@loren lb]# kubectl delete -f nginx_lb.yaml
```


### 2. 通过OCI LB访问Nginx

准备配置文件

```
[root@loren lb]# cat nginx-demo-svc-ssl.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
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
        image: nginx
        ports:
        - containerPort: 80
---
kind: Service
apiVersion: v1
metadata:
  name: nginx-service
  annotations:
    oci.oraclecloud.com/load-balancer-type: "lb"
    service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
    service.beta.kubernetes.io/oci-load-balancer-tls-secret: ssl-certificate-secret
spec:
  selector:
    app: nginx
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 80
    
```

准备并创建证书，注意这个证书是为OCI LB指定端口添加的证书，可以为多个端口添加指定的TLS证书，详细可以看上面的注释。

```
[root@loren lb]# openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=nginxsvc/O=nginxsvc"
Generating a RSA private key
...........................+++++
.............................+++++
writing new private key to 'tls.key'
-----
[root@loren lb]# ls
nginx-demo-svc-ssl.yaml  nginx_lb.yaml  tls.crt  tls.key
[root@loren lb]# kubectl create secret tls ssl-certificate-secret --key tls.key --cert tls.crt
secret/ssl-certificate-secret created
```
部署

```
[root@loren lb]# kubectl create -f nginx-demo-svc-ssl.yaml
deployment.apps/nginx-deployment created
service/nginx-service created
```
查看部署进展

```
[root@loren lb]# kc get all
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-7f456874f4-jpxx8   1/1     Running   0          87s
pod/nginx-deployment-7f456874f4-wds7k   1/1     Running   0          87s

NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
service/kubernetes      ClusterIP      10.96.0.1       <none>           443/TCP,12250/TCP            104m
service/nginx-service   LoadBalancer   10.96.110.191   150.230.204.62   80:31992/TCP,443:31928/TCP   87s

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   2/2     2            2           87s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-7f456874f4   2         2         2       87s
[root@loren lb]# kubectl get all
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-7f456874f4-jpxx8   1/1     Running   0          96s
pod/nginx-deployment-7f456874f4-wds7k   1/1     Running   0          96s

NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
service/kubernetes      ClusterIP      10.96.0.1       <none>           443/TCP,12250/TCP            104m
service/nginx-service   LoadBalancer   10.96.110.191   150.230.204.62   80:31992/TCP,443:31928/TCP   96s

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   2/2     2            2           96s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-7f456874f4   2         2         2       96s
```
验证

```
[root@loren lb]# curl -I http://150.230.204.62
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 09:45:57 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

[root@loren lb]# curl -I --insecure https://150.230.204.62
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 09:46:07 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

```

证书更新

```
[root@loren lb]# mkdir -p new
[root@loren lb]# cd new
[root@loren new]#  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=nginxsvc/O=nginxsvc"
Generating a RSA private key
.............+++++
.............................................................+++++
writing new private key to 'tls.key'
-----
[root@loren new]# kubectl create secret tls new-ssl-certificate-secret --key tls.key --cert tls.crt
secret/new-ssl-certificate-secret created
```

更新配置，试用新的证书

```
[root@loren new]# cat new-nginx-demo-svc-ssl.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  annotations:
    service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
    service.beta.kubernetes.io/oci-load-balancer-tls-secret: new-ssl-certificate-secret
spec:
  selector:
    app: nginx
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 80
```

删除先前得`service`,创建试用新证书得`service`

```
[root@loren new]# kubectl delete svc nginx-service
service "nginx-service" deleted

[root@loren new]# kubectl apply -f new-nginx-demo-svc-ssl.yaml
service/nginx-service created
```

查看状态

```
[root@loren new]# kubectl get svc
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
kubernetes      ClusterIP      10.96.0.1       <none>          443/TCP,12250/TCP            114m
nginx-service   LoadBalancer   10.96.127.127   158.101.67.11   80:30282/TCP,443:32560/TCP   2m35s

```

验证

```
[root@loren new]# curl -I http://158.101.67.11
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 09:55:43 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

[root@loren new]# curl -I --insecure https://158.101.67.11
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 09:55:57 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

```

### 3. 更新LB的规格

注意， 以上指定的LB都是固定规格的，即默认带宽为100Mbps
OCI建议试用Flexible规格的LB，默认最高带宽为25Gbps,更大的带宽还可以再申请。

```
[root@loren new]# cat new-nginx-demo-svc-ssl.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  annotations:
    service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
    service.beta.kubernetes.io/oci-load-balancer-shape: "flexible"
    service.beta.kubernetes.io/oci-load-balancer-shape-flex-min: "10"
    service.beta.kubernetes.io/oci-load-balancer-shape-flex-max: "100"
    service.beta.kubernetes.io/oci-load-balancer-tls-secret: new-ssl-certificate-secret
spec:
  selector:
    app: nginx
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 80
[root@loren new]# kubectl apply -f new-nginx-demo-svc-ssl.yaml
service/nginx-service configured

```

验证

```
[root@loren new]# kubectl get svc
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
kubernetes      ClusterIP      10.96.0.1       <none>          443/TCP,12250/TCP            129m
nginx-service   LoadBalancer   10.96.127.127   158.101.67.11   80:30282/TCP,443:32560/TCP   17m
[root@loren new]# curl -I --insecure https://158.101.67.11
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 10:10:53 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes
```

另外，还支持指定LB连接超时时间、监听协议、安全列表等，如

```
    service.beta.kubernetes.io/oci-load-balancer-connection-idle-timeout: 100
    service.beta.kubernetes.io/oci-load-balancer-backend-protocol: "HTTP"
    service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode: "Frontend"
```

如果没有明确指定最长空闲时间，则会使用默认值。默认值取决于侦听器的类型：
- 对于 TCP 侦听器，默认最大空闲时间为 300 秒
- 对于 HTTP 侦听器，默认最大空闲时间为 60 秒

### 3. 固定LB的IP

在实际生产中，希望LB的公网IP地址能够固定，以避免必要风险，这里可以使用OCI提供的预留IP。

首先在OCI界面上(`Networking>IP Management>Reserved Public IPs`)先申请预留IP,然后将IP地址填写到配置文件中即可。

```
[root@loren new]# cat new-nginx-demo-svc-ssl.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  annotations:
    service.beta.kubernetes.io/oci-load-balancer-ssl-ports: "443"
    service.beta.kubernetes.io/oci-load-balancer-shape: "flexible"
    service.beta.kubernetes.io/oci-load-balancer-shape-flex-min: "10"
    service.beta.kubernetes.io/oci-load-balancer-shape-flex-max: "100"
    service.beta.kubernetes.io/oci-load-balancer-tls-secret: new-ssl-certificate-secret
spec:
  selector:
    app: nginx
  type: LoadBalancer
  loadBalancerIP: 158.101.71.121
  ports:
  - name: http
    port: 80
    targetPort: 80
  - name: https
    port: 443
    targetPort: 80

```

删除重建service

```
[root@loren new]# kubectl delete -f new-nginx-demo-svc-ssl.yaml
service "nginx-service" deleted
[root@loren new]# kubectl apply -f new-nginx-demo-svc-ssl.yaml
service/nginx-service created
[root@loren new]# kubectl get svc --watch
NAME            TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
kubernetes      ClusterIP      10.96.0.1      <none>        443/TCP,12250/TCP            148m
nginx-service   LoadBalancer   10.96.223.43   <pending>     80:32224/TCP,443:30590/TCP   7s
nginx-service   LoadBalancer   10.96.223.43   158.101.71.121   80:32224/TCP,443:30590/TCP   44s

```

验证

```
[root@loren new]# curl -I --insecure https://158.101.71.121
HTTP/1.1 200 OK
Server: nginx/1.23.4
Date: Wed, 24 May 2023 10:31:12 GMT
Content-Type: text/html
Content-Length: 615
Last-Modified: Tue, 28 Mar 2023 15:01:54 GMT
Connection: keep-alive
ETag: "64230162-267"
Accept-Ranges: bytes

```

