
## Python-rdis调用

环境准备

```
pip3 install redis
```

示例代码如下：

```

>>> import redis
>>>
>>> ssl_connection = redis.Redis(host='amaaaaaapyxxcxcxcxcccccccccpweq-p.redis.ap-chuncheon-1.oci.oraclecloud.com', port=6379, ssl=True, ssl_cert_reqs="none")
>>> ssl_connection.ping()
True

```
