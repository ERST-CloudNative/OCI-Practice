
安装示例应用

```

[root@d01 ~]# kubectl apply -f https://raw.githubusercontent.com/cert-manager/website/master/content/docs/tutorials/acme/example/deployment.yaml
deployment.apps/kuard created
[root@d01 ~]# kubectl apply -f https://raw.githubusercontent.com/cert-manager/website/master/content/docs/tutorials/acme/example/service.yaml
service/kuard created
[root@d01 ~]# wget https://raw.githubusercontent.com/cert-manager/website/master/content/docs/tutorials/acme/example/ingress.yaml^C
[root@d01 ~]# kc get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
kuard        ClusterIP   10.96.104.120   <none>        80/TCP              51s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP,12250/TCP   91m
[root@d01 ~]# kc create ingress kuard --class=nginx --rule="www.demo.io/*=kuard:80"
ingress.networking.k8s.io/kuard created
[root@d01 ~]# kubectl get ingress
NAME    CLASS   HOSTS         ADDRESS         PORTS   AGE
kuard   nginx   www.demo.io   146.56.97.126   80      17s

```

默认的是HTTP协议，80端口，验证web访问正常

<img width="727" alt="1702890789309" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/93457e87-6573-42a2-9ce9-ad2e91a96d5d">


安装Helm

```
[root@d01 ~]# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
[root@d01 ~]# chmod 700 get_helm.sh
[root@d01 ~]# ./get_helm.sh

Helm v3.13.1 is already latest

```









