### 1. 排查SLB对options方法是否有特定限制

选择NGINX作为后端服务器，模拟提供OPTIONS操作
```
        location / {
            if ($request_method = OPTIONS ) {
                add_header Content-Length 0;
                add_header Content-Type text/plain;
                return 200;
            }
            add_header Access-Control-Allow-Origin *;
            add_header Access-Control-Max-Age 3600;
            add_header Access-Control-Expose-Headers Content-Length;
            add_header Access-Control-Allow-Headers Range;
        }

```

测试正常

```
$ curl -Ivs -X OPTIONS http://138.2.44.237:80
HTTP/1.1 200 OK
Date: Thu, 14 Jul 2022 07:24:11 GMT
Content-Type: text/plain
Content-Length: 0
Connection: keep-alive

*   Trying 138.2.44.237:80...
* Connected to 138.2.44.237 (138.2.44.237) port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: 138.2.44.237
> User-Agent: curl/7.78.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 14 Jul 2022 07:24:11 GMT
< Content-Type: text/plain
< Content-Length: 0
< Connection: keep-alive
<
* Connection #0 to host 138.2.44.237 left intact
```

切换使用国内的网络访问

```
$ time curl -Ivs -X OPTIONS http://140.83.63.223:80
HTTP/1.1 200 OK
Date: Thu, 14 Jul 2022 07:36:45 GMT
Content-Type: text/plain
Content-Length: 0
Connection: keep-alive

*   Trying 140.83.63.223:80...
* Connected to 140.83.63.223 (140.83.63.223) port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: 140.83.63.223
> User-Agent: curl/7.78.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 14 Jul 2022 07:36:45 GMT
< Content-Type: text/plain
< Content-Length: 0
< Connection: keep-alive
<
* Connection #0 to host 140.83.63.223 left intact

real    0m0.878s
user    0m0.000s
sys     0m0.015s
```

### 2. 排查K8S集群内部网络

#### 2.1 带宽测试，跨节点pod-pod

```
[root@bootstrap ~]# alias kc=kubectl
[root@bootstrap ~]# kc -n demo exec -it nginx-netshoot-776dff49d-9vp2r -c netshoot -- /bin/zsh
Unable to connect to the server: net/http: TLS handshake timeout
[root@bootstrap ~]# kc -n demo exec -it nginx-netshoot-776dff49d-9vp2r -c netshoot -- /bin/zsh
                    dP            dP                           dP
                    88            88                           88
88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P
88'  `88 88ooood8   88   Y8ooooo. 88'  `88 88'  `88 88'  `88   88
88    88 88.  ...   88         88 88    88 88.  .88 88.  .88   88
dP    dP `88888P'   dP   `88888P' dP    dP `88888P' `88888P'   dP

Welcome to Netshoot! (github.com/nicolaka/netshoot)

 nginx-netshoot-776dff49d-9vp2r  ~  iperf -s -p 9999
------------------------------------------------------------
Server listening on TCP port 9999
TCP window size:  128 KByte (default)
------------------------------------------------------------
[  1] local 172.20.72.184 port 9999 connected with 172.20.33.21 port 48846
[ ID] Interval       Transfer     Bandwidth
[  1] 0.00-10.01 sec   730 MBytes   611 Mbits/sec
[  2] local 172.20.72.184 port 9999 connected with 172.20.33.21 port 52202
[ ID] Interval       Transfer     Bandwidth
[  2] 0.00-10.01 sec   731 MBytes   612 Mbits/sec
```

```
[root@bootstrap ~]# kc -n demo get pods -o wide
NAME                             READY   STATUS    RESTARTS   AGE   IP              NODE            NOMINATED NODE   READINESS GATES
netshoot-64bb958d4f-s6jdm        1/1     Running   0          27m   172.20.33.6     10.100.10.135   <none>           <none>
nginx-netshoot-776dff49d-9vp2r   2/2     Running   0          15m   172.20.72.184   10.100.10.173   <none>           <none>
nginx-netshoot-776dff49d-s4vgj   2/2     Running   0          19m   172.20.33.21    10.100.10.135   <none>           <none>

[root@bootstrap ~]# kc -n demo exec -it nginx-netshoot-776dff49d-s4vgj -c netshoot -- /bin/zsh
                    dP            dP                           dP
                    88            88                           88
88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P
88'  `88 88ooood8   88   Y8ooooo. 88'  `88 88'  `88 88'  `88   88
88    88 88.  ...   88         88 88    88 88.  .88 88.  .88   88
dP    dP `88888P'   dP   `88888P' dP    dP `88888P' `88888P'   dP

Welcome to Netshoot! (github.com/nicolaka/netshoot)



 nginx-netshoot-776dff49d-s4vgj  ~  iperf -c 172.20.72.184 -p 9999
------------------------------------------------------------
Client connecting to 172.20.72.184, TCP port 9999
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  1] local 172.20.33.21 port 48846 connected with 172.20.72.184 port 9999
[ ID] Interval       Transfer     Bandwidth
[  1] 0.00-10.02 sec   730 MBytes   611 Mbits/sec

 nginx-netshoot-776dff49d-s4vgj  ~  iperf -c 172.20.72.184 -p 9999
------------------------------------------------------------
Client connecting to 172.20.72.184, TCP port 9999
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  1] local 172.20.33.21 port 52202 connected with 172.20.72.184 port 9999
[ ID] Interval       Transfer     Bandwidth
[  1] 0.00-10.02 sec   731 MBytes   612 Mbits/sec
```

#### 2.2 抓包验证

后端依然使用nginx默认http服务，验证跨节点pod-pod L7网络访问通信正常

```
nginx-netshoot-776dff49d-9vp2r  ~  tcpdump -nvvv -i eth0 -w debug.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
Got 2045
```

```
nginx-netshoot-776dff49d-s4vgj  ~  for i in {1..100} do\ncurl -I 172.20.72.184
```

![image](https://user-images.githubusercontent.com/4653664/178944465-27ced8e1-5feb-43e8-82b1-4ebdbb9899da.png)

#### 2.3 域名解析服务

验证集群内网域名解析正常

```
[root@bootstrap ~]# kc -n demo exec -it nginx-netshoot-776dff49d-9vp2r -c netshoot -- /bin/zsh
                    dP            dP                           dP
                    88            88                           88
88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P
88'  `88 88ooood8   88   Y8ooooo. 88'  `88 88'  `88 88'  `88   88
88    88 88.  ...   88         88 88    88 88.  .88 88.  .88   88
dP    dP `88888P'   dP   `88888P' dP    dP `88888P' `88888P'   dP

Welcome to Netshoot! (github.com/nicolaka/netshoot)

 nginx-netshoot-776dff49d-s4vgj  ~  drill -V 5 kodo-inner.forethought-kodo.svc.cluster.local
;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 0
;; flags: rd ; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; kodo-inner.forethought-kodo.svc.cluster.local.       IN      A

;; ANSWER SECTION:

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 0 msec
;; WHEN: Thu Jul 14 08:42:08 2022
;; MSG SIZE  rcvd: 0
;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 44702
;; flags: qr aa rd ; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; kodo-inner.forethought-kodo.svc.cluster.local.       IN      A

;; ANSWER SECTION:
kodo-inner.forethought-kodo.svc.cluster.local.  30      IN      A       192.68.82.235

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 3 msec
;; SERVER: 169.254.20.10
;; WHEN: Thu Jul 14 08:42:08 2022
;; MSG SIZE  rcvd: 124
```

```
nginx-netshoot-776dff49d-9vp2r  ~  drill -V 5 df-api.test.com
;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 0
;; flags: rd ; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; df-api.test.com.     IN      A

;; ANSWER SECTION:

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 0 msec
;; WHEN: Thu Jul 14 09:09:33 2022
;; MSG SIZE  rcvd: 0
;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 19022
;; flags: qr rd ra ; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; df-api.test.com.     IN      A

;; ANSWER SECTION:
df-api.test.com.        30      IN      A       69.167.164.199

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 9 msec
;; SERVER: 169.254.20.10
;; WHEN: Thu Jul 14 09:09:33 2022
;; MSG SIZE  rcvd: 64

 nginx-netshoot-776dff49d-9vp2r  ~  ping 69.167.164.199
PING 69.167.164.199 (69.167.164.199) 56(84) bytes of data.
64 bytes from 69.167.164.199: icmp_seq=9 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=10 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=11 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=12 ttl=59 time=24.1 ms
64 bytes from 69.167.164.199: icmp_seq=13 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=14 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=15 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=16 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=17 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=18 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=19 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=20 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=21 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=22 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=23 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=24 ttl=59 time=23.9 ms
64 bytes from 69.167.164.199: icmp_seq=25 ttl=59 time=23.8 ms
64 bytes from 69.167.164.199: icmp_seq=26 ttl=59 time=23.9 ms

```
