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


部署 `Nginx Ingress`

```
[root@loren lb]# kubectl apply -f ingress-nginx.yaml

```

