
网络问题调试

```
[root@loren ]# kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot

```

获取证书

```
$ openssl s_client -showcerts -host 127.0.0.1 -port 9200
```

证书有效期查验

```
[root@loren ~]# openssl s_client -showcerts -connect 132.226.15.10:6443 | openssl x509 -text
...
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            55:84:8c:77:e3:82:fe:b6:a6:4d:df:79:3c:f8:e5:40
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = K8s CA, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
        Validity
            Not Before: May 29 08:30:09 2023 GMT
            Not After : May 29 08:30:09 2028 GMT
        Subject: CN = kubernetes.default, C = US, L = Austin, O = Oracle, OU = Oci, ST = Texas
...
```

节点网络调试

```
[root@loren lb]# kubectl debug node/10.0.10.129 -it --image=nicolaka/netshoot

#                                                                                                                                                       
 oke-csvmwhzny2a-ndn5exlyjmq-sz7wyqlrmma-2  ~  netstat -ntlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:10248         0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:9003          0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:37651         0.0.0.0:*               LISTEN      -
tcp        0      0 ::ffff:127.0.0.1:32768  :::*                    LISTEN      -
tcp        0      0 :::30401                :::*                    LISTEN      -
tcp        0      0 :::10249                :::*                    LISTEN      -
tcp        0      0 :::10250                :::*                    LISTEN      -
tcp        0      0 :::10256                :::*                    LISTEN      -
tcp        0      0 :::111                  :::*                    LISTEN      -
tcp        0      0 :::22                   :::*                    LISTEN      -
#                                                                                                                                                       
 oke-csvmwhzny2a-ndn5exlyjmq-sz7wyqlrmma-2  ~  ping google.com
PING google.com (142.250.196.142) 56(84) bytes of data.
64 bytes from nrt12s36-in-f14.1e100.net (142.250.196.142): icmp_seq=1 ttl=122 time=1.66 ms
64 bytes from nrt12s36-in-f14.1e100.net (142.250.196.142): icmp_seq=2 ttl=122 time=1.72 ms
64 bytes from nrt12s36-in-f14.1e100.net (142.250.196.142): icmp_seq=3 ttl=122 time=1.76 ms
^C
--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 1.657/1.711/1.755/0.040 ms

```
