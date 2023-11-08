
## Redis连接网络抓包过程

TLS握手流程

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f1b044c8-de12-4550-83d3-e6c2ee6052cd)


最前面是TCP连接的三次握手，后面TLS握手

<img width="955" alt="1699437681372" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/46a07f40-fcd5-4789-84c5-3dbc24778592">

以上对应的redis操作命令为：

```
root@test003:~# redis-cli --tls -h amaaaaasaapyx7sfqaaseeembg3p3jzvakcgtaspweq-p.redis.ap-chuncheon-1.oci.oraclecloud.com
amaaaaaapyx7sfaswjv3bmre5as3fheeecasjzvakcgtsasqpweq-p.redis.ap-chuncheon-1.oci.oraclecloud.com:6379> 
```

如果没有使用--tls，则会遇到以下异常情况，默认服务器端已经开启TLS

<img width="962" alt="1699438566090" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1e1d5afe-7e5a-4ba3-8a1c-4973675dfae1">

```
[root@hy redis-7.0.14]# redis-cli -h amaaadfdfacybyfddfddrvqm6lvsjdeoh4ycdfdfdsdrfydrxrar2nrq-r.redis.ap-chuncheon-1.oci.o
amaaadfdfdfdfdm6lvsjdeoh4yddfdcxcdfdfydrxrar2nrq-r.rdfis.ap-chuncheon-1.oci.oraclecloud.com:6379> scan
Error: Connection reset by peer
```

接下来对redis进行读写操作，再详细看下抓包信息

```
amaaaaaapyx7wewewwembg3p3weweweweeh2tqpweq-p.redis.ap-chuncheon-1.oci.oraclecloud.com:6379> set name loren
OK
amaaaaaapywewefheeemwep3jzvakcgtgvh2tqpweq-p.redis.ap-chuncheon-1.oci.oraclecloud.com:6379> get name
"loren"
```

<img width="932" alt="1699438304209" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/7088524e-d400-4dbb-b2aa-49804a2467a4">
