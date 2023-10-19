## OKE集群升级

> 通常为了保持集群的安全性，k8S集群需要定期更新升级。

查看证书的有效期

```
[root@loren ~]# openssl s_client -showcerts -connect 158.178.245.224:6443 | openssl x509 -text
...
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            06:7a:dd:dd:ac:73:a5:ab:d7:dc:6b:34:b4:d5:da:19
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = K8s CA, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
        Validity
            Not Before: May 30 11:02:09 2023 GMT
            Not After : May 30 11:02:09 2028 GMT
        Subject: CN = kubernetes.default, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
...

```

查看是否有更新的版本

<img width="954" alt="1685445161053" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b54745a9-74a7-4008-aa6d-f46a22724a33">


选择可更新的版本，点击`Upgrade`

<img width="950" alt="1685445203622" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/4d88cf8b-95ec-4943-be25-d10a668423ec">

<img width="959" alt="1685445289835" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/36d20e8d-e9bf-482e-8a8a-a75b1b8fdd31">

等待集群更新完成

<img width="946" alt="1685445959168" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ec6cbd0b-b4e1-4c23-be2d-056fd30aaa25">

查看证书的有效期，对比升级前，证书重新签发。

```
[root@loren ~]# openssl s_client -showcerts -connect 158.178.245.224:6443 | openssl x509 -text
...
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            af:42:65:22:54:f3:ab:be:12:6b:d1:bf:36:fb:2f:64
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = K8s CA, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
        Validity
            Not Before: May 30 11:21:33 2023 GMT
            Not After : May 30 11:21:33 2028 GMT
        Subject: CN = kubernetes.default, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
...
```











