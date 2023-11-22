

## OCI镜像仓库配置


1. 获取token，即docker login时提供的密码

```
控制台获取路径：Identity > My profile > Auth tokens
```
2. 设置权限策略

创建一个名为`acme-managers`的用户组，并将对应的用户添加到用户组中，然后配置以下策略

```
Allow group acme-managers to manage repos in tenancy
```

3. 创建镜像仓库，并查看所在区域的镜像仓库地址

```
https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability
```

4. 权限验证

```
# 登录镜像仓库
[root@redis01 ~]# docker login yny.ocir.io
Username: axv8ifpuvrvl/lodsei.ren@oracle.com
Password:
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

# 打包镜像
[root@redis01 ~]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        1.14.2    295c7be07902   4 years ago   109MB
[root@redis01 ~]# docker tag 295c7be07902 yny.ocir.io/axv8ifpuvrvl/test/nginx:1.14.2

[root@redis01 ~]# docker images
REPOSITORY                            TAG       IMAGE ID       CREATED       SIZE
nginx                                 1.14.2    295c7be07902   4 years ago   109MB
yny.ocir.io/axv8ifpuvrvl/test/nginx   1.14.2    295c7be07902   4 years ago   109MB

# 推送镜像
[root@redis01 ~]# docker push yny.ocir.io/axv8ifpuvrvl/test/nginx:1.14.2
The push refers to repository [yny.ocir.io/axv8ifpuvrvl/test/nginx]
82ae01d5004e: Pushed
b8f18c3b860b: Pushed
5dacd731af1b: Pushed
1.14.2: digest: sha256:706446e9c6667c0880d5da3f39c09a6c7d2114f5a5d6b74a2fafd24ae30d2078 size: 948
```

5. 验证OKE集成

```
# 创建secret
[root@redis01 ~]# kubectl create secret docker-registry docker-registry-secret \
  --docker-server="yny.ocir.io" \
  --docker-username="[NameSpace]/[UserName]" \
  --docker-password="[YOUR AUTH TOKEN]" \
  --docker-email="[YOUR Email]"

secret/docker-registry-secret created

# 将secret与serviceaccount绑定
[root@redis01 ~]# kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "docker-registry-secret"}]}'
serviceaccount/default patched

[root@redis01 ~]# cat nginx-demo.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: yny.ocir.io/axv8ifpuvrvl/test/nginx:1.14.2
        ports:
        - containerPort: 80

[root@redis01 ~]# kubectl apply -f nginx-demo.yaml
deployment.apps/nginx-deployment created
[root@redis01 ~]# alias kc=kubectl
[root@redis01 ~]# kc get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-76bcd6765c-744zp   1/1     Running   0          19s
nginx-deployment-76bcd6765c-zn2mw   1/1     Running   0          19s

[root@redis01 ~]# kubectl describe pod nginx-deployment-76bcd6765c-744zp
...
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  42s   default-scheduler  Successfully assigned default/nginx-deployment-76bcd6765c-744zp to 10.0.10.216
  Normal  Pulling    41s   kubelet            Pulling image "yny.ocir.io/axv8ifpuvrvl/test/nginx:1.14.2"
  Normal  Pulled     39s   kubelet            Successfully pulled image "yny.ocir.io/axv8ifpuvrvl/test/nginx:1.14.2" in 2.538627061s (2.538643062s including waiting)
  Normal  Created    39s   kubelet            Created container nginx
  Normal  Started    39s   kubelet            Started container nginx

```

