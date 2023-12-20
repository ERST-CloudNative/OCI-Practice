
## OKE集群升级

控制平面升级：
- 默认提供界面操作，选择需要升级的预期版本即可，这里需要注意是否有配置在新版本不可用的情况
- 一般情况下，控制平面升级并不会影响业务，建议在升级前做好备份工作，以备不时之需。

节点版本升级三种方案：
- 新增节点池，手动驱离旧的节点池中的pods
- 回收节点,就地升级，可以配置相关策略，过程自动化完成操作
- 手动升级节点，手动按需操作

```
[root@d01 ~]# kc get nodes
NAME          STATUS     ROLES   AGE     VERSION
10.0.65.142   Ready      node    5h15m   v1.26.7
10.0.65.164   NotReady   node    76s     v1.28.2
10.0.65.240   Ready      node    5h15m   v1.26.7
10.0.65.94    Ready      node    5h15m   v1.26.7
10.0.66.18    NotReady   node    45s     v1.28.2
10.0.66.94    NotReady   node    84s     v1.28.2
[root@d01 ~]# kc get nodes
NAME          STATUS     ROLES    AGE     VERSION
10.0.64.16    Ready      node     2m57s   v1.28.2
10.0.64.168   NotReady   <none>   34s     v1.28.2
10.0.65.164   Ready      node     10m     v1.28.2
10.0.65.169   Ready      node     5m50s   v1.28.2
10.0.66.18    Ready      node     9m31s   v1.28.2
10.0.66.94    Ready      node     10m     v1.28.2
[root@d01 ~]# kc -n ingress-nginx get pods -o wide
NAME                                        READY   STATUS    RESTARTS   AGE   IP           NODE         NOMINATED NODE   READINESS GATES
ingress-nginx-controller-6599b4f4c5-86rxw   1/1     Running   0          96s   10.0.40.69   10.0.64.16   <none>           <none>
[root@d01 ~]# kc get nodes
NAME          STATUS   ROLES   AGE     VERSION
10.0.64.16    Ready    node    4m18s   v1.28.2
10.0.64.168   Ready    node    115s    v1.28.2
10.0.65.164   Ready    node    11m     v1.28.2
10.0.65.169   Ready    node    7m11s   v1.28.2
10.0.66.18    Ready    node    10m     v1.28.2
10.0.66.94    Ready    node    11m     v1.28.2

```

在节点就地升级过程中，由于需要驱离原有节点上的pod，所以会导致短时间业务中断，所以建议选择合适的时间窗口进行操作。

```
[root@d01 ~]# while true; do curl -I  -X GET http://www.demo.io/; sleep 2; done

HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:35:21 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (52) Empty reply from server
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:16 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:18 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
curl: (52) Empty reply from server
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:24 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:28 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
curl: (56) Recv failure: Connection reset by peer
curl: (52) Empty reply from server
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:36 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:40 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

curl: (56) Recv failure: Connection reset by peer
HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:44 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:46 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

HTTP/1.1 200 OK
Date: Wed, 20 Dec 2023 13:36:48 GMT
Content-Type: text/html
Content-Length: 615
Connection: keep-alive
Last-Modified: Tue, 24 Oct 2023 13:46:47 GMT
ETag: "6537cac7-267"
Accept-Ranges: bytes

```
