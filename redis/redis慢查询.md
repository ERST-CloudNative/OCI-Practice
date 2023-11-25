## Redis慢查询


1. 确认Redis慢查询的相关配置

```
slowlog-log-slower-than 10000
slowlog-max-len 1000
```

2. 写入大量数据

```
# pip install redis

import redis
import random
import string

# 连接到本地 Redis 服务器
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 写入大量数据
for i in range(100000):
    # 生成随机的数据内容，超过 100 个字节
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=150))

    # 构造键名
    key = f"mykey_{i}"

    # 写入数据到 Redis
    redis_client.set(key, data)

print("数据写入完成")

```

3. 获取所有键（耗时操作）

```
127.0.0.1:6379> keys *
```

在另一个终端，执行慢查询命令

```
127.0.0.1:6379> SLOWLOG get 5
1) 1) (integer) 0
   2) (integer) 1700911784
   3) (integer) 26367
   4) 1) "keys"
      2) "*"
   5) "127.0.0.1:41928"
   6) ""
```

