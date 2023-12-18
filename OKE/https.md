
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


```
[root@d01 ~]# kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.3/cert-manager.crds.yaml
customresourcedefinition.apiextensions.k8s.io/certificaterequests.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/certificates.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/challenges.acme.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/clusterissuers.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/issuers.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/orders.acme.cert-manager.io created
[root@d01 ~]# helm install   cert-manager jetstack/cert-manager   --namespace cert-manager   --create-namespace   --version v1.13.3                     WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /root/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /root/.kube/config
NAME: cert-manager
LAST DEPLOYED: Mon Dec 18 10:48:11 2023
NAMESPACE: cert-manager
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
cert-manager v1.13.3 has been deployed successfully!

In order to begin issuing certificates, you will need to set up a ClusterIssuer
or Issuer resource (for example, by creating a 'letsencrypt-staging' issuer).

More information on the different types of issuers and how to configure them
can be found in our documentation:

https://cert-manager.io/docs/configuration/

For information on how to configure cert-manager to automatically provision
Certificates for Ingress resources, take a look at the `ingress-shim`
documentation:

https://cert-manager.io/docs/usage/ingress/


```








