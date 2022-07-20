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

### 3. 存储性能排查

#### 3.1 自建K8S+OCI文件服务

##### 4K-随机读

```
# fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 512MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=86.8MiB/s][r=22.2k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=16: Wed Jul 20 04:27:45 2022
  read: IOPS=21.8k, BW=85.0MiB/s (89.2MB/s)(5103MiB/60006msec)
    slat (nsec): min=1012, max=3401.2k, avg=7064.31, stdev=14367.89
    clat (usec): min=1016, max=27630, avg=5869.35, stdev=1031.20
     lat (usec): min=1034, max=27643, avg=5876.61, stdev=1031.26
    clat percentiles (usec):
     |  1.00th=[ 3720],  5.00th=[ 4359], 10.00th=[ 4686], 20.00th=[ 5014],
     | 30.00th=[ 5342], 40.00th=[ 5604], 50.00th=[ 5800], 60.00th=[ 6063],
     | 70.00th=[ 6325], 80.00th=[ 6652], 90.00th=[ 7111], 95.00th=[ 7570],
     | 99.00th=[ 8455], 99.50th=[ 8979], 99.90th=[11076], 99.95th=[13304],
     | 99.99th=[22414]
   bw (  KiB/s): min=77626, max=94320, per=100.00%, avg=87138.13, stdev=4922.80, samples=119
   iops        : min=19406, max=23580, avg=21784.50, stdev=1230.70, samples=119
  lat (msec)   : 2=0.02%, 4=2.10%, 10=97.70%, 20=0.17%, 50=0.01%
  cpu          : usr=5.88%, sys=18.64%, ctx=708778, majf=0, minf=137
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1306494,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=85.0MiB/s (89.2MB/s), 85.0MiB/s-85.0MiB/s (89.2MB/s-89.2MB/s), io=5103MiB (5351MB), run=60006-60006msec
```

##### 4K-随机写

```
# fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=44.5MiB/s][w=11.4k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=19: Wed Jul 20 04:30:04 2022
  write: IOPS=11.2k, BW=43.7MiB/s (45.8MB/s)(2623MiB/60010msec); 0 zone resets
    slat (nsec): min=1163, max=2850.3k, avg=7593.56, stdev=10100.48
    clat (usec): min=3702, max=32576, avg=11430.97, stdev=1188.29
     lat (usec): min=3705, max=32579, avg=11438.77, stdev=1188.25
    clat percentiles (usec):
     |  1.00th=[ 9372],  5.00th=[ 9896], 10.00th=[10159], 20.00th=[10421],
     | 30.00th=[10814], 40.00th=[10945], 50.00th=[11207], 60.00th=[11600],
     | 70.00th=[11863], 80.00th=[12256], 90.00th=[12911], 95.00th=[13566],
     | 99.00th=[14746], 99.50th=[15664], 99.90th=[18744], 99.95th=[20055],
     | 99.99th=[22414]
   bw (  KiB/s): min=40048, max=48128, per=100.00%, avg=44781.83, stdev=1889.45, samples=119
   iops        : min=10012, max=12032, avg=11195.45, stdev=472.36, samples=119
  lat (msec)   : 4=0.01%, 10=7.14%, 20=92.81%, 50=0.05%
  cpu          : usr=3.41%, sys=10.43%, ctx=305936, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,671403,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=43.7MiB/s (45.8MB/s), 43.7MiB/s-43.7MiB/s (45.8MB/s-45.8MB/s), io=2623MiB (2750MB), run=60010-60010msec
```

##### 1M-随机读

```
# fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=231MiB/s][r=231 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=22: Wed Jul 20 04:31:56 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60566msec)
    slat (usec): min=34, max=2484, avg=61.75, stdev=37.60
    clat (msec): min=35, max=1011, avg=537.25, stdev=116.86
     lat (msec): min=35, max=1012, avg=537.31, stdev=116.85
    clat percentiles (msec):
     |  1.00th=[  150],  5.00th=[  368], 10.00th=[  384], 20.00th=[  414],
     | 30.00th=[  443], 40.00th=[  558], 50.00th=[  575], 60.00th=[  600],
     | 70.00th=[  617], 80.00th=[  634], 90.00th=[  659], 95.00th=[  676],
     | 99.00th=[  709], 99.50th=[  743], 99.90th=[  995], 99.95th=[ 1003],
     | 99.99th=[ 1011]
   bw (  KiB/s): min=143360, max=358163, per=99.69%, avg=243119.22, stdev=58112.96, samples=120
   iops        : min=  140, max=  349, avg=237.41, stdev=56.73, samples=120
  lat (msec)   : 50=0.08%, 100=0.35%, 250=0.69%, 500=34.88%, 750=63.60%
  lat (msec)   : 1000=0.35%, 2000=0.06%
  cpu          : usr=0.15%, sys=1.63%, ctx=14637, majf=0, minf=583
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14425,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60566-60566msec
```

##### 1M-随机写

```
# fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=25: Wed Jul 20 04:34:07 2022
  write: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60539msec); 0 zone resets
    slat (usec): min=45, max=1634, avg=83.06, stdev=28.99
    clat (msec): min=16, max=1072, avg=537.17, stdev=42.37
     lat (msec): min=16, max=1072, avg=537.26, stdev=42.38
    clat percentiles (msec):
     |  1.00th=[  514],  5.00th=[  514], 10.00th=[  514], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  550], 95.00th=[  550],
     | 99.00th=[  567], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=159744, max=256000, per=99.81%, avg=243457.46, stdev=9059.96, samples=120
   iops        : min=  156, max=  250, avg=237.75, stdev= 8.85, samples=120
  lat (msec)   : 20=0.01%, 50=0.06%, 100=0.09%, 250=0.26%, 500=0.44%
  lat (msec)   : 750=98.61%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.70%, sys=1.64%, ctx=14529, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14421,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60539-60539msec
```

##### dd工具测试

```
# dd if=/dev/zero of=./testdd1 bs=4k count=1024 oflag=dsync
1024+0 records in
1024+0 records out
4194304 bytes (4.2 MB, 4.0 MiB) copied, 3.26621 s, 1.3 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 32.0579 s, 1.3 MB/s

# dd if=/dev/zero of=./testdd1 bs=4M count=10 oflag=dsync
10+0 records in
10+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 0.349764 s, 120 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=25600 oflag=dsync
25600+0 records in
25600+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 80.6019 s, 1.3 MB/s
```

#### 3.2 OKE+块存储(StorageClass) 

这部分环境使用OKE集群，并使用OCI原生提供的块存储。

查看挂载信息

```
longfei_re@cloudshell:~ (ap-osaka-1)$ kc exec -it fio-pv-pod -- /bin/sh
/ # df -hT
Filesystem           Type            Size      Used Available Use% Mounted on
overlay              overlay        38.4G      6.9G     31.4G  18% /
tmpfs                tmpfs          64.0M         0     64.0M   0% /dev
tmpfs                tmpfs           7.7G         0      7.7G   0% /sys/fs/cgroup
shm                  tmpfs          64.0M         0     64.0M   0% /dev/shm
tmpfs                tmpfs           7.7G     32.6M      7.6G   0% /etc/resolv.conf
tmpfs                tmpfs           7.7G     32.6M      7.6G   0% /etc/hostname
tmpfs                tmpfs           7.7G     32.6M      7.6G   0% /run/.containerenv
/dev/sdb             ext4           49.1G     52.0M     46.5G   0% /scratch
/dev/sda3            xfs            38.4G      6.9G     31.4G  18% /etc/hosts
/dev/sda3            xfs            38.4G      6.9G     31.4G  18% /dev/termination-log
tmpfs                tmpfs          15.2G     12.0K     15.2G   0% /run/secrets/kubernetes.io/serviceaccount
tmpfs                tmpfs           7.7G         0      7.7G   0% /proc/acpi
tmpfs                tmpfs          64.0M         0     64.0M   0% /proc/kcore
tmpfs                tmpfs          64.0M         0     64.0M   0% /proc/keys
tmpfs                tmpfs          64.0M         0     64.0M   0% /proc/timer_list
tmpfs                tmpfs          64.0M         0     64.0M   0% /proc/sched_debug
tmpfs                tmpfs           7.7G         0      7.7G   0% /proc/scsi
tmpfs                tmpfs           7.7G         0      7.7G   0% /sys/firmware
```

##### 4K-随机读

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 512MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=11.3MiB/s][r=2885 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=18: Wed Jul 20 05:07:47 2022
  read: IOPS=3125, BW=12.2MiB/s (12.8MB/s)(733MiB/60054msec)
    slat (nsec): min=1753, max=1055.5k, avg=7805.10, stdev=5356.43
    clat (usec): min=398, max=395631, avg=40943.54, stdev=26132.41
     lat (usec): min=413, max=395641, avg=40951.55, stdev=26132.41
    clat percentiles (usec):
     |  1.00th=[  1647],  5.00th=[  5342], 10.00th=[  9634], 20.00th=[ 17957],
     | 30.00th=[ 25822], 40.00th=[ 32900], 50.00th=[ 39060], 60.00th=[ 45351],
     | 70.00th=[ 52167], 80.00th=[ 60031], 90.00th=[ 72877], 95.00th=[ 83362],
     | 99.00th=[107480], 99.50th=[147850], 99.90th=[233833], 99.95th=[261096],
     | 99.99th=[325059]
   bw (  KiB/s): min=11112, max=29793, per=99.87%, avg=12484.38, stdev=2324.00, samples=119
   iops        : min= 2778, max= 7448, avg=3121.11, stdev=580.98, samples=119
  lat (usec)   : 500=0.01%, 750=0.12%, 1000=0.20%
  lat (msec)   : 2=1.06%, 4=2.20%, 10=6.79%, 20=12.19%, 50=44.56%
  lat (msec)   : 100=31.60%, 250=1.22%, 500=0.06%
  cpu          : usr=1.47%, sys=6.34%, ctx=179254, majf=0, minf=140
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=187695,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=12.2MiB/s (12.8MB/s), 12.2MiB/s-12.2MiB/s (12.8MB/s-12.8MB/s), io=733MiB (769MB), run=60054-60054msec

Disk stats (read/write):
  sdb: ios=185455/8, merge=1975/6, ticks=7600191/164, in_queue=7502693, util=99.96%
```

##### 4K-随机写

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=11.6MiB/s][w=2968 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=21: Wed Jul 20 05:09:26 2022
  write: IOPS=2992, BW=11.7MiB/s (12.3MB/s)(702MiB/60027msec); 0 zone resets
    slat (nsec): min=1764, max=77038k, avg=107568.13, stdev=1614112.02
    clat (usec): min=970, max=184543, avg=42671.92, stdev=24251.31
     lat (usec): min=974, max=184545, avg=42779.60, stdev=24273.10
    clat percentiles (msec):
     |  1.00th=[    3],  5.00th=[    6], 10.00th=[   12], 20.00th=[   23],
     | 30.00th=[   30], 40.00th=[   35], 50.00th=[   41], 60.00th=[   45],
     | 70.00th=[   53], 80.00th=[   63], 90.00th=[   73], 95.00th=[   91],
     | 99.00th=[  110], 99.50th=[  118], 99.90th=[  133], 99.95th=[  146],
     | 99.99th=[  161]
   bw (  KiB/s): min= 9864, max=38927, per=99.57%, avg=11917.03, stdev=2617.06, samples=119
   iops        : min= 2466, max= 9731, avg=2979.25, stdev=654.20, samples=119
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.22%, 4=2.75%, 10=5.57%, 20=8.31%, 50=51.07%
  lat (msec)   : 100=29.62%, 250=2.45%
  cpu          : usr=0.43%, sys=1.76%, ctx=4693, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,179601,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=11.7MiB/s (12.3MB/s), 11.7MiB/s-11.7MiB/s (12.3MB/s-12.3MB/s), io=702MiB (736MB), run=60027-60027msec

Disk stats (read/write):
  sdb: ios=0/183547, merge=0/3601, ticks=0/2930981, in_queue=2837663, util=99.96%
```


##### 1M-随机读

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=24: Wed Jul 20 05:10:54 2022
  read: IOPS=24, BW=24.1MiB/s (25.2MB/s)(1575MiB/65459msec)
    slat (usec): min=12, max=455, avg=40.98, stdev=35.51
    clat (msec): min=13, max=16375, avg=5315.73, stdev=3557.62
     lat (msec): min=13, max=16375, avg=5315.77, stdev=3557.62
    clat percentiles (msec):
     |  1.00th=[   91],  5.00th=[ 1452], 10.00th=[ 1620], 20.00th=[ 2005],
     | 30.00th=[ 2601], 40.00th=[ 3406], 50.00th=[ 4463], 60.00th=[ 5738],
     | 70.00th=[ 7080], 80.00th=[ 8490], 90.00th=[10671], 95.00th=[12013],
     | 99.00th=[14697], 99.50th=[15905], 99.90th=[16040], 99.95th=[16442],
     | 99.99th=[16442]
   bw (  KiB/s): min=16384, max=86646, per=99.42%, avg=24495.92, stdev=5833.15, samples=120
   iops        : min=   16, max=   84, avg=23.92, stdev= 5.64, samples=120
  lat (msec)   : 20=0.13%, 50=0.32%, 100=1.02%, 250=1.46%, 500=0.38%
  lat (msec)   : 750=0.38%, 1000=0.38%, 2000=15.81%, >=2000=80.13%
  cpu          : usr=0.01%, sys=0.16%, ctx=1575, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.5%, 16=1.0%, 32=2.0%, >=64=96.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1575,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=24.1MiB/s (25.2MB/s), 24.1MiB/s-24.1MiB/s (25.2MB/s-25.2MB/s), io=1575MiB (1652MB), run=65459-65459msec

Disk stats (read/write):
  sdb: ios=1569/3, merge=0/1, ticks=7991836/5257, in_queue=7996177, util=99.90%
```


##### 1M-随机写

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][eta 00m:00s]                       
Fio: (groupid=0, jobs=1): err= 0: pid=27: Wed Jul 20 05:12:27 2022
  write: IOPS=23, BW=23.0MiB/s (25.2MB/s)(1454MiB/60614msec); 0 zone resets
    slat (usec): min=25, max=4384.9k, avg=3092.64, stdev=114997.77
    clat (msec): min=4002, max=10702, avg=5332.57, stdev=1213.42
     lat (msec): min=4002, max=10702, avg=5335.67, stdev=1221.02
    clat percentiles (msec):
     |  1.00th=[ 4010],  5.00th=[ 4010], 10.00th=[ 4329], 20.00th=[ 4530],
     | 30.00th=[ 4665], 40.00th=[ 5269], 50.00th=[ 5403], 60.00th=[ 5403],
     | 70.00th=[ 5403], 80.00th=[ 5470], 90.00th=[ 5470], 95.00th=[ 9731],
     | 99.00th=[10134], 99.50th=[10537], 99.90th=[10537], 99.95th=[10671],
     | 99.99th=[10671]
   bw (  KiB/s): min=206848, max=262144, per=100.00%, avg=246877.09, stdev=20507.91, samples=11
   iops        : min=  202, max=  256, avg=241.09, stdev=20.03, samples=11
  lat (msec)   : >=2000=100.00%
  cpu          : usr=0.07%, sys=0.04%, ctx=46, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.3%, 8=0.6%, 16=1.1%, 32=2.2%, >=64=95.7%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1454,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=23.0MiB/s (25.2MB/s), 23.0MiB/s-23.0MiB/s (25.2MB/s-25.2MB/s), io=1454MiB (1525MB), run=60614-60614msec

Disk stats (read/write):
  sdb: ios=0/1478, merge=0/15, ticks=0/4040169, in_queue=4039438, util=99.84%
```

##### dd测试

```
# df -hT
Filesystem     Type     Size  Used Avail Use% Mounted on
overlay        overlay   39G  7.1G   32G  19% /
tmpfs          tmpfs     64M     0   64M   0% /dev
tmpfs          tmpfs    7.7G     0  7.7G   0% /sys/fs/cgroup
shm            tmpfs     64M     0   64M   0% /dev/shm
tmpfs          tmpfs    7.7G   33M  7.7G   1% /etc/hostname
/dev/sda3      xfs       39G  7.1G   32G  19% /etc/hosts
/dev/sdb       ext4      50G  153M   47G   1% /usr/share/nginx/html
tmpfs          tmpfs     16G   12K   16G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs          tmpfs    7.7G     0  7.7G   0% /proc/acpi
tmpfs          tmpfs    7.7G     0  7.7G   0% /proc/scsi
tmpfs          tmpfs    7.7G     0  7.7G   0% /sys/firmware

# dd if=/dev/zero of=./testdd1 bs=4k count=1024 oflag=dsync
1024+0 records in
1024+0 records out
4194304 bytes (4.2 MB, 4.0 MiB) copied, 1.31985 s, 3.2 MB/s
# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 14.107 s, 3.0 MB/s
# dd if=/dev/zero of=./testdd1 bs=4M count=10 oflag=dsync
10+0 records in
10+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 0.183204 s, 229 MB/s
# dd if=/dev/zero of=./testdd1 bs=4k count=25600 oflag=dsync
25600+0 records in
25600+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 34.4532 s, 3.0 MB/s

```

3.3 OKE+高性能卷存储

##### 4K-随机读

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 512MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=13.0MiB/s][r=3577 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=18: Wed Jul 20 08:40:09 2022
  read: IOPS=3903, BW=15.2MiB/s (15.0MB/s)(916MiB/60064msec)
    slat (nsec): min=1983, max=325591, avg=8954.19, stdev=5909.89
    clat (usec): min=329, max=135133, avg=32778.80, stdev=33583.76
     lat (usec): min=341, max=135142, avg=32787.96, stdev=33583.75
    clat percentiles (usec):
     |  1.00th=[   938],  5.00th=[  1532], 10.00th=[  2147], 20.00th=[  3425],
     | 30.00th=[  4883], 40.00th=[  6980], 50.00th=[ 14484], 60.00th=[ 34866],
     | 70.00th=[ 49546], 80.00th=[ 70779], 90.00th=[ 90702], 95.00th=[ 93848],
     | 99.00th=[ 98042], 99.50th=[ 99091], 99.90th=[105382], 99.95th=[107480],
     | 99.99th=[117965]
   bw (  KiB/s): min=13824, max=37389, per=99.71%, avg=15568.26, stdev=2929.36, samples=119
   iops        : min= 3456, max= 9347, avg=3892.06, stdev=732.33, samples=119
  lat (usec)   : 500=0.03%, 750=0.25%, 1000=0.96%
  lat (msec)   : 2=7.49%, 4=15.39%, 10=21.89%, 20=7.18%, 50=17.13%
  lat (msec)   : 100=29.28%, 250=0.40%
  cpu          : usr=1.93%, sys=8.42%, ctx=219990, majf=0, minf=139
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=234466,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=15.2MiB/s (15.0MB/s), 15.2MiB/s-15.2MiB/s (15.0MB/s-15.0MB/s), io=916MiB (960MB), run=60064-60064msec

Disk stats (read/write):
  sdb: ios=233975/8, merge=486/6, ticks=7662125/163, in_queue=7545300, util=99.99%
```

##### 4K-随机写

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=14.3MiB/s][w=3665 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=21: Wed Jul 20 08:41:46 2022
  write: IOPS=3721, BW=14.5MiB/s (15.2MB/s)(873MiB/60056msec); 0 zone resets
    slat (usec): min=2, max=88118, avg=95.62, stdev=1680.20
    clat (usec): min=685, max=145633, avg=34297.42, stdev=28891.38
     lat (usec): min=691, max=145640, avg=34393.22, stdev=28906.90
    clat percentiles (usec):
     |  1.00th=[  1418],  5.00th=[  1909], 10.00th=[  2278], 20.00th=[  3195],
     | 30.00th=[ 10683], 40.00th=[ 26084], 50.00th=[ 32113], 60.00th=[ 35914],
     | 70.00th=[ 40633], 80.00th=[ 58983], 90.00th=[ 82314], 95.00th=[ 90702],
     | 99.00th=[104334], 99.50th=[109577], 99.90th=[122160], 99.95th=[125305],
     | 99.99th=[131597]
   bw (  KiB/s): min=12200, max=47346, per=99.58%, avg=14822.13, stdev=3143.30, samples=119
   iops        : min= 3050, max=11836, avg=3705.53, stdev=785.78, samples=119
  lat (usec)   : 750=0.01%, 1000=0.09%
  lat (msec)   : 2=5.96%, 4=18.42%, 10=5.24%, 20=5.26%, 50=41.42%
  lat (msec)   : 100=21.75%, 250=1.85%
  cpu          : usr=0.75%, sys=3.41%, ctx=7535, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,223497,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=14.5MiB/s (15.2MB/s), 14.5MiB/s-14.5MiB/s (15.2MB/s-15.2MB/s), io=873MiB (915MB), run=60056-60056msec

Disk stats (read/write):
  sdb: ios=0/230375, merge=0/3518, ticks=0/2558886, in_queue=2437900, util=99.98%
```


##### 1M-随机读

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][eta 00m:00s]                        
Fio: (groupid=0, jobs=1): err= 0: pid=24: Wed Jul 20 08:44:44 2022
  read: IOPS=30, BW=30.3MiB/s (31.8MB/s)(1950MiB/64359msec)
    slat (usec): min=12, max=630, avg=39.62, stdev=40.54
    clat (msec): min=16, max=8924, avg=4221.68, stdev=1225.68
     lat (msec): min=17, max=8924, avg=4221.72, stdev=1225.66
    clat percentiles (msec):
     |  1.00th=[  136],  5.00th=[ 1116], 10.00th=[ 3943], 20.00th=[ 4044],
     | 30.00th=[ 4111], 40.00th=[ 4212], 50.00th=[ 4279], 60.00th=[ 4396],
     | 70.00th=[ 4463], 80.00th=[ 4665], 90.00th=[ 4933], 95.00th=[ 5671],
     | 99.00th=[ 8020], 99.50th=[ 8423], 99.90th=[ 8792], 99.95th=[ 8926],
     | 99.99th=[ 8926]
   bw (  KiB/s): min=18432, max=130756, per=99.23%, avg=30785.63, stdev=9313.07, samples=120
   iops        : min=   18, max=  127, avg=30.06, stdev= 9.03, samples=120
  lat (msec)   : 20=0.05%, 50=0.26%, 100=0.41%, 250=2.97%, 500=0.36%
  lat (msec)   : 750=0.36%, 1000=0.41%, 2000=1.59%, >=2000=93.59%
  cpu          : usr=0.04%, sys=0.16%, ctx=1951, majf=0, minf=588
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=0.4%, 16=0.8%, 32=1.6%, >=64=96.8%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1950,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=30.3MiB/s (31.8MB/s), 30.3MiB/s-30.3MiB/s (31.8MB/s-31.8MB/s), io=1950MiB (2045MB), run=64359-64359msec

Disk stats (read/write):
  sdb: ios=1946/3, merge=0/1, ticks=7941340/2983, in_queue=7943361, util=99.91%
```


##### 1M-随机写

```
~ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=1022KiB/s][w=0 IOPS][eta 00m:00s] 
Fio: (groupid=0, jobs=1): err= 0: pid=27: Wed Jul 20 08:45:55 2022
  write: IOPS=29, BW=29.9MiB/s (31.4MB/s)(1891MiB/63156msec); 0 zone resets
    slat (usec): min=28, max=2663.2k, avg=4383.07, stdev=90998.50
    clat (msec): min=1442, max=9570, avg=4269.38, stdev=686.71
     lat (msec): min=1671, max=9570, avg=4273.77, stdev=687.06
    clat percentiles (msec):
     |  1.00th=[ 2937],  5.00th=[ 2937], 10.00th=[ 3373], 20.00th=[ 4279],
     | 30.00th=[ 4329], 40.00th=[ 4329], 50.00th=[ 4329], 60.00th=[ 4329],
     | 70.00th=[ 4329], 80.00th=[ 4329], 90.00th=[ 4396], 95.00th=[ 5269],
     | 99.00th=[ 8221], 99.50th=[ 8423], 99.90th=[ 9597], 99.95th=[ 9597],
     | 99.99th=[ 9597]
   bw (  KiB/s): min= 2048, max=262144, per=100.00%, avg=180633.60, stdev=108150.98, samples=20
   iops        : min=    2, max=  256, avg=176.40, stdev=105.62, samples=20
  lat (msec)   : 2000=0.11%, >=2000=99.89%
  cpu          : usr=0.09%, sys=0.08%, ctx=83, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=0.4%, 16=0.8%, 32=1.7%, >=64=96.7%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,1891,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=29.9MiB/s (31.4MB/s), 29.9MiB/s-29.9MiB/s (31.4MB/s-31.4MB/s), io=1891MiB (1983MB), run=63156-63156msec

Disk stats (read/write):
  sdb: ios=0/1920, merge=0/18, ticks=0/3951669, in_queue=3950707, util=99.91%
```
##### dd测试

```
# df -hT
Filesystem     Type     Size  Used Avail Use% Mounted on
overlay        overlay   39G  7.2G   32G  19% /
tmpfs          tmpfs     64M     0   64M   0% /dev
tmpfs          tmpfs    7.7G     0  7.7G   0% /sys/fs/cgroup
shm            tmpfs     64M     0   64M   0% /dev/shm
tmpfs          tmpfs    7.7G   33M  7.7G   1% /etc/hostname
/dev/sda3      xfs       39G  7.2G   32G  19% /etc/hosts
/dev/sdc       ext4      50G   53M   47G   1% /usr/share/nginx/html
tmpfs          tmpfs     16G   12K   16G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs          tmpfs    7.7G     0  7.7G   0% /proc/acpi
tmpfs          tmpfs    7.7G     0  7.7G   0% /proc/scsi
tmpfs          tmpfs    7.7G     0  7.7G   0% /sys/firmware
# cd /usr/share/nginx/html
# pwd
/usr/share/nginx/html
# dd if=/dev/zero of=./testdd1 bs=4k count=1024 oflag=dsync
1024+0 records in
1024+0 records out
4194304 bytes (4.2 MB, 4.0 MiB) copied, 1.34994 s, 3.1 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 13.5051 s, 3.1 MB/s

# dd if=/dev/zero of=./testdd1 bs=4M count=10 oflag=dsync
10+0 records in
10+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 0.188951 s, 222 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=25600 oflag=dsync
25600+0 records in
25600+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 34.5483 s, 3.0 MB/s

```


#### 3.4 OKE + NFS(OCI)

##### 4K-随机读

```
/ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Fio: Laying out IO file (1 file / 512MiB)
Jobs: 1 (f=1): [r(1)][100.0%][r=106MiB/s][r=27.1k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=15: Wed Jul 20 10:48:41 2022
  read: IOPS=24.8k, BW=97.0MiB/s (102MB/s)(5822MiB/60004msec)
    slat (nsec): min=1332, max=1387.7k, avg=9118.16, stdev=11171.85
    clat (usec): min=1115, max=17261, avg=5142.30, stdev=825.06
     lat (usec): min=1124, max=17267, avg=5151.63, stdev=825.22
    clat percentiles (usec):
     |  1.00th=[ 3458],  5.00th=[ 3916], 10.00th=[ 4178], 20.00th=[ 4490],
     | 30.00th=[ 4686], 40.00th=[ 4883], 50.00th=[ 5080], 60.00th=[ 5276],
     | 70.00th=[ 5473], 80.00th=[ 5735], 90.00th=[ 6194], 95.00th=[ 6587],
     | 99.00th=[ 7504], 99.50th=[ 7963], 99.90th=[ 9372], 99.95th=[10159],
     | 99.99th=[11600]
   bw (  KiB/s): min=84520, max=114496, per=100.00%, avg=99392.23, stdev=7965.69, samples=119
   iops        : min=21130, max=28624, avg=24848.05, stdev=1991.42, samples=119
  lat (msec)   : 2=0.01%, 4=6.13%, 10=93.81%, 20=0.06%
  cpu          : usr=6.45%, sys=23.70%, ctx=287324, majf=0, minf=136
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=1490389,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=97.0MiB/s (102MB/s), 97.0MiB/s-97.0MiB/s (102MB/s-102MB/s), io=5822MiB (6105MB), run=60004-60004msec
```

##### 4K-随机写

```
/ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=4K -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=49.0MiB/s][w=12.8k IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=18: Wed Jul 20 10:51:14 2022
  write: IOPS=12.2k, BW=47.6MiB/s (49.9MB/s)(2854MiB/60009msec); 0 zone resets
    slat (nsec): min=1673, max=586841, avg=11007.84, stdev=9695.25
    clat (usec): min=4013, max=43918, avg=10500.02, stdev=1300.37
     lat (usec): min=4033, max=43928, avg=10511.26, stdev=1300.45
    clat percentiles (usec):
     |  1.00th=[ 8586],  5.00th=[ 8979], 10.00th=[ 9241], 20.00th=[ 9503],
     | 30.00th=[ 9765], 40.00th=[10028], 50.00th=[10290], 60.00th=[10552],
     | 70.00th=[10945], 80.00th=[11469], 90.00th=[11994], 95.00th=[12518],
     | 99.00th=[14091], 99.50th=[15270], 99.90th=[19792], 99.95th=[26084],
     | 99.99th=[39584]
   bw (  KiB/s): min=43512, max=53048, per=100.00%, avg=48731.55, stdev=2813.78, samples=119
   iops        : min=10878, max=13262, avg=12182.88, stdev=703.44, samples=119
  lat (msec)   : 10=38.80%, 20=61.11%, 50=0.10%
  cpu          : usr=4.44%, sys=16.23%, ctx=262304, majf=0, minf=9
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,730615,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=47.6MiB/s (49.9MB/s), 47.6MiB/s-47.6MiB/s (49.9MB/s-49.9MB/s), io=2854MiB (2993MB), run=60009-60009msec
```


##### 1M-随机读

```
/ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randread -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [r(1)][100.0%][r=262MiB/s][r=261 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=21: Wed Jul 20 10:54:37 2022
  read: IOPS=238, BW=238MiB/s (250MB/s)(14.1GiB/60571msec)
    slat (usec): min=42, max=470, avg=89.27, stdev=30.66
    clat (msec): min=36, max=1140, avg=537.22, stdev=115.64
     lat (msec): min=36, max=1140, avg=537.31, stdev=115.64
    clat percentiles (msec):
     |  1.00th=[  165],  5.00th=[  363], 10.00th=[  376], 20.00th=[  409],
     | 30.00th=[  439], 40.00th=[  567], 50.00th=[  575], 60.00th=[  592],
     | 70.00th=[  609], 80.00th=[  625], 90.00th=[  659], 95.00th=[  676],
     | 99.00th=[  709], 99.50th=[  802], 99.90th=[  869], 99.95th=[  877],
     | 99.99th=[ 1133]
   bw (  KiB/s): min=139264, max=391901, per=99.67%, avg=243069.58, stdev=59465.20, samples=120
   iops        : min=  136, max=  382, avg=237.37, stdev=58.06, samples=120
  lat (msec)   : 50=0.02%, 100=0.21%, 250=0.95%, 500=32.59%, 750=65.57%
  lat (msec)   : 1000=0.64%, 2000=0.01%
  cpu          : usr=0.18%, sys=2.64%, ctx=14440, majf=0, minf=584
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=14426,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
   READ: bw=238MiB/s (250MB/s), 238MiB/s-238MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60571-60571msec
```


##### 1M-随机写

```
/ # fio -numjobs=1 -iodepth=128 -direct=1 -ioengine=libaio -sync=1 -rw=randwrite -bs=1M -size=512M -time_based -runtime=60 -name=Fio -directory=/scratch
Fio: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=128
fio-3.19
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][w=237MiB/s][w=236 IOPS][eta 00m:00s]
Fio: (groupid=0, jobs=1): err= 0: pid=24: Wed Jul 20 10:56:26 2022
  write: IOPS=238, BW=239MiB/s (250MB/s)(14.1GiB/60540msec); 0 zone resets
    slat (usec): min=58, max=398, avg=115.66, stdev=25.55
    clat (msec): min=15, max=1073, avg=536.42, stdev=42.38
     lat (msec): min=15, max=1073, avg=536.54, stdev=42.38
    clat percentiles (msec):
     |  1.00th=[  514],  5.00th=[  514], 10.00th=[  514], 20.00th=[  535],
     | 30.00th=[  542], 40.00th=[  542], 50.00th=[  542], 60.00th=[  542],
     | 70.00th=[  542], 80.00th=[  542], 90.00th=[  542], 95.00th=[  542],
     | 99.00th=[  558], 99.50th=[  768], 99.90th=[ 1011], 99.95th=[ 1045],
     | 99.99th=[ 1070]
   bw (  KiB/s): min=153600, max=256000, per=99.82%, avg=243796.50, stdev=9470.18, samples=120
   iops        : min=  150, max=  250, avg=238.07, stdev= 9.24, samples=120
  lat (msec)   : 20=0.01%, 50=0.05%, 100=0.10%, 250=0.26%, 500=0.44%
  lat (msec)   : 750=98.61%, 1000=0.41%, 2000=0.12%
  cpu          : usr=0.99%, sys=2.45%, ctx=14448, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.2%, >=64=99.6%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.1%
     issued rwts: total=0,14440,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=128

Run status group 0 (all jobs):
  WRITE: bw=239MiB/s (250MB/s), 239MiB/s-239MiB/s (250MB/s-250MB/s), io=14.1GiB (15.1GB), run=60540-60540msec
```

##### dd测试

```
# df -hT
Filesystem                                                                                            Type     Size  Used Avail Use% Mounted on
overlay                                                                                               overlay   39G  7.1G   32G  19% /
tmpfs                                                                                                 tmpfs     64M     0   64M   0% /dev
tmpfs                                                                                                 tmpfs    7.7G     0  7.7G   0% /sys/fs/cgroup
shm                                                                                                   tmpfs     64M     0   64M   0% /dev/shm
tmpfs                                                                                                 tmpfs    7.7G   33M  7.7G   1% /etc/hostname
/dev/sda3                                                                                             xfs       39G  7.1G   32G  19% /etc/hosts
10.0.20.93:/FileSystem-20220720-0954-37/default-nfs-pv-claim-pvc-34b2774b-82e0-492a-860c-e7337c20cb1a nfs      8.0E     0  8.0E   0% /usr/share/nginx/html
tmpfs                                                                                                 tmpfs     16G   12K   16G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs                                                                                                 tmpfs    7.7G     0  7.7G   0% /proc/acpi
tmpfs                                                                                                 tmpfs    7.7G     0  7.7G   0% /proc/scsi
tmpfs                                                                                                 tmpfs    7.7G     0  7.7G   0% /sys/firmware
# cd /usr/share/nginx/html
# ls

# dd if=/dev/zero of=./testdd1 bs=4k count=1024 oflag=dsync
1024+0 records in
1024+0 records out
4194304 bytes (4.2 MB, 4.0 MiB) copied, 1.43847 s, 2.9 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=10240 oflag=dsync
10240+0 records in
10240+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 27.8512 s, 1.5 MB/s

# dd if=/dev/zero of=./testdd1 bs=4M count=10 oflag=dsync
10+0 records in
10+0 records out
41943040 bytes (42 MB, 40 MiB) copied, 0.384129 s, 109 MB/s

# dd if=/dev/zero of=./testdd1 bs=4k count=25600 oflag=dsync
25600+0 records in
25600+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 68.2638 s, 1.5 MB/s
```
