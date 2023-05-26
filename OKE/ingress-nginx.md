## Nginx Ingress方案

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

可以通过修改`ingress-nginx.yaml`中的参数来调整LB带宽

```
    service.beta.kubernetes.io/oci-load-balancer-shape: "400Mbps"
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

测试验证

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















