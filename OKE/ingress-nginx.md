## Nginx Ingress方案-L7

### 部署Nginx Ingress

给部分计算节点打标签，以部署`Nginx ingress controller` `pod`。

```
[root@loren lb]# kubectl get nodes
NAME          STATUS   ROLES   AGE     VERSION
10.0.10.134   Ready    node    3h30m   v1.26.2
10.0.10.15    Ready    node    3h30m   v1.26.2
10.0.10.64    Ready    node    3h30m   v1.26.2

[root@loren lb]# kubectl label node 10.0.10.134 ingress=nginx
[root@loren lb]# kubectl label node 10.0.10.15 ingress=nginx
```
> ingress-nginx是经过编辑的，所以需要做以上配置
> 未经过修改的配置文件地址：https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.7.1/deploy/static/provider/cloud/deploy.yaml

可以通过修改`ingress-nginx.yaml`中的参数来调整LB带宽、指定预留IP等

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.7.1
  annotations:
    oci.oraclecloud.com/load-balancer-type: "lb"
    service.beta.kubernetes.io/oci-load-balancer-shape: "400Mbps"
    oci.oraclecloud.com/node-label-selector: ingress=nginx
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  externalTrafficPolicy: Local
  loadBalancerIP: 158.101.71.121
```

部署 `Nginx Ingress`，并扩容`ingress-nginx-controller`个数

```
[root@loren lb]# kubectl apply -f ingress-nginx.yaml
[root@loren lb]# kubectl -n ingress-nginx scale deployment/ingress-nginx-controller --replicas=2
```

验证是否可以获取预留的公网IP地址，并且确认LB的带宽

```
[root@loren lb]# kc -n ingress-nginx get svc
NAME                                 TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
ingress-nginx-controller             LoadBalancer   10.96.191.155   158.101.71.121   80:31860/TCP,443:31108/TCP   6m2s
ingress-nginx-controller-admission   ClusterIP      10.96.19.40     <none>           443/TCP                      19m
```

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d5476df9-275c-4dca-bd0b-5540d17a9aeb)

### 配置防火墙

这里需要开放的端口有：

转发端口：30779，31410
健康检查端口：30799


<img width="942" alt="1af846f4c008605aad301d96e0eed65" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/38c0919a-e73a-4c16-afcc-4a23f41d37b4">

<img width="893" alt="eaff1eaab85c46cff0c6d188c2b1065" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/80c042e6-ce14-4d55-bbe2-2763c9be106c">

<img width="901" alt="333b4efd7bd90b6cda89cf660c9792b" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/bad59114-a6cd-462e-bdab-a047aeae0b55">

<img width="945" alt="1685431322329" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6e0750fc-3669-4bb6-b6ba-c22803934077">


检查相关端口是否开通，如果没有，可以通过以下方式手动开通相关端口。


<img width="713" alt="83c145d55d5f077fd78dfad07708822" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8476c22d-3a61-4dae-9372-8d8080067376">

<img width="733" alt="968686628403d877522528a4a5856eb" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/48fcb8a4-acdb-4880-b634-f6fc8ee14b91">

<img width="956" alt="f0a8fa1fb6acc6717bbadec42c0a990" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8c0677e9-88c5-4be4-8a77-2fccb75c99b2">


### 测试验证

```
[root@loren lb]# kubectl create deployment demo --image=httpd --port=80
[root@loren lb]# kubectl expose deployment demo
[root@loren lb]# kubectl create ingress demo --class=nginx --rule="www.demo.io/*=demo:80"
[root@loren lb]# echo "158.101.71.121 www.demo.io" >> /etc/hosts
[root@loren lb]# curl www.demo.io
<html><body><h1>It works!</h1></body></html>
```

## Prometheus监控

部署`Prometheus`

```
$ git clone https://github.com/prometheus-operator/kube-prometheus.git
$ cd kube-prometheus/
$ kubectl create -f manifests/setup
$ until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
$ kubectl create -f manifests/
$ kubectl -n monitoring get pods
```

创建`ingress`

```
[root@loren lb]# kubectl create ingress grafana --class=nginx --rule="grafana.loren/*=grafana:3000" -n monitoring
[root@loren lb]# kubectl create ingress prometheus-k8s --class=nginx --rule="prom.loren/*=prometheus-k8s:9090" -n monitoring
```

> grafana默认账户密码 admin:admin

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/addce00f-1b3d-4d27-a4b8-c7e098159aff)

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/301450e4-d65f-4156-86ac-d9e048f31552)

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/56a0aa58-043a-4219-bd44-6b2cb79daba3)

## 日志(Fluentd-OpenSearch)

`OpenSearch`集群的创建参考上一级目录下的`opensearch.md`

部署`fluentd`,其中`fluentd-daemonset-opensearch.yaml`中的需要填写`opensearch`的用户名、密码、`API endpoint`等信息

```
[root@loren ~]# kubectl apply -f fluentd.configmap
[root@loren ~]# kubectl apply -f fluentd-daemonset-opensearch.yaml
```

访问`Opensearch Dashboard`，参考上一级目录下的`bastion.md`

<img width="960" alt="1685108229782" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8a984c63-24f2-40c6-b5d2-c172040b2d4f">

<img width="956" alt="1685108136257" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/0894633c-b39b-4fa0-987b-a06f6f4853e7">

回到`Discover`页面

<img width="960" alt="1685108291876" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1522fdde-3b7d-4235-8f23-bdf300c5c138">


创建过滤条件，这里我们查看指定pod的日志信息。

<img width="948" alt="1685107654678" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/a019e2ec-df01-443a-b886-a1fba0c13ffb">

## Nginx Ingress方案-L4

删除L7 LB
```
[root@loren lb]# kubectl -n ingress-nginx delete svc ingress-nginx-controller
```

创建L4 LB(Network LoadBalancer)

```
[root@loren lb]# cat ingress-nlb.yaml
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.7.1
  annotations:
    oci.oraclecloud.com/load-balancer-type: "nlb"
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  externalTrafficPolicy: Local
  loadBalancerIP: 155.248.184.230
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - appProtocol: http
    name: http
    port: 80
    protocol: TCP
    targetPort: http
  - appProtocol: https
    name: https
    port: 443
    protocol: TCP
    targetPort: https
  selector:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  type: LoadBalancer

[root@loren lb]# kubectl apply -f ingress-nlb.yaml
```

因为LB转发监听节点端口，所以这里需要开通子网的防火墙

<img width="927" alt="1685361196092" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/14e218c1-0dc8-442b-8495-570f4782454e">

<img width="879" alt="1685361224136" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d56d45ac-fe72-47d4-8465-0688e8a94d01">


这里需要明确添加哪些端口，这里主要有三个端口：
80映射端口
443映射端口
健康检查端口

<img width="940" alt="b734383eab9d7b9501d475b5f01a1c7" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/65aa6812-9d02-401c-903b-e3f6d308e335">
<img width="937" alt="a21ec4a9d241aac867828f790a971a3" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f0e3d054-c6be-4d65-901f-cff3837c9e3c">
<img width="951" alt="c1b4cbdbab252069196ad4b39dc148b" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f3e1b585-5a31-4d05-b632-1901fa910e6c">

添加出站规则

<img width="950" alt="1685361887380" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f1e2f079-74f2-4b69-87fc-76bc64bf00c3">

<img width="946" alt="1685361936758" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1d00b6c7-4dfe-4587-87de-8caed59999ff">

验证

```
[root@loren lb]# curl www.demo.io
<html><body><h1>It works!</h1></body></html>

```











