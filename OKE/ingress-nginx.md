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

创建`ingress`

```
[root@loren lb]# kubectl create ingress grafana --class=nginx --rule="grafana.loren/*=grafana:3000" -n monitoring
[root@loren lb]# kubectl create ingress prometheus-k8s --class=nginx --rule="prom.loren/*=prometheus-k8s:9090" -n monitoring
```

> grafana默认账户密码 admin:admin

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/addce00f-1b3d-4d27-a4b8-c7e098159aff)

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/301450e4-d65f-4156-86ac-d9e048f31552)

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/56a0aa58-043a-4219-bd44-6b2cb79daba3)


