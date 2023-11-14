## Redis


### 1. Redis配置


通过命令行修改redis配置

```
> CONFIG get maxclients
1) "maxclients"
2) "10000"

> CONFIG set maxclients 1000
OK

> CONFIG get maxclients
1) "maxclients"
2) "1000"

```

> `config get *` 将获取所有的配置信息

### 2. Redis数据类型

1. 字符串

Redis 字符串是一个字节序列。Redis 中的字符串是二进制安全的，这意味着它们具有已知长度，不由任何特殊终止字符确定。因此，您可以在一个字符串中存储最多 512 MB的任何内容。

```
>  SET name "tutorialspoint"
OK
> get name
"tutorialspoint"
```

2. 哈希值

Redis 哈希是键值对的集合。Redis 哈希是字符串字段和字符串值之间的映射。因此，它们被用来表示对象。

```
> hmset user1 username loren pass 123
OK
> hgetall user1
1) "username"
2) "loren"
3) "pass"
4) "123"

```

3. 列表

Redis 列表只是字符串列表，按插入顺序排序。您可以将元素添加到 Redis 列表的头部或尾部。

```
> lpush test math
(integer) 1
> lpush test eng
(integer) 2
> lpush test science
(integer) 3
> lrange test 0 10
1) "science"
2) "eng"
3) "math"

```

列表的最大长度为 2 32 - 1 个元素（4294967295，每个列表超过 40 亿个元素）。

4. 集合

Redis 集是无序的字符串集合。在 Redis 中，您可以以 O(1) 的时间复杂度添加、删除成员以及测试成员是否存在。

```
> sadd test2 redis
(integer) 1
> sadd test2 mongodb
(integer) 1
> sadd test2 rabbitmq
(integer) 1
> sadd test2 rabbitmq
(integer) 0
> smembers test2
1) "rabbitmq"
2) "redis"
3) "mongodb"
```

注意- 在上面的示例中，rabbitmq添加了两次，但是由于集合的独特属性，它只添加了一次,在一定程度可以起到去重的目的。

集合中的最大成员数为 2 32 - 1（4294967295，每个集合超过 40 亿个成员）。

5. 排序集合

Redis 排序集类似于 Redis 集，即非重复的字符串集合。不同之处在于，排序集的每个成员都与一个分数相关联，用于对排序集进行从最小到最大分数的排序。虽然成员是独一无二的，但分数可能会重复。

```

> zadd test3 0 redis
(integer) 1
> zadd test3 2 mongodb
(integer) 1
> zadd test3 1 rabbitmq
(integer) 1
> zadd test3 1 rabbitmq
(integer) 0
> zrangebyscore test3 0 100
1) "redis"
2) "rabbitmq"
3) "mongodb"

```

### 3. Redis命令

1. 服务器连接

```
$ redis-cli -h host -p port -a password
```

2. redids keys

创建、删除、检查键是否存在

```
> set a 123
OK
> del a
(integer) 1
> exists a
(integer) 0

```

设置键有3秒的到期时间

```
> set b 123
OK
> exists b
(integer) 1
> expire b 3
(integer) 1
> exists b
(integer) 0

```

设置到期时间，不断查询余下的时间，然后中途移除键的到期时间

```
> set c 123
OK
> expire c 60
(integer) 1
> ttl c
(integer) 57
> ttl c
(integer) 55
> ttl c
(integer) 53
> type c
string
> ttl c
(integer) 25
> pttl c
(integer) 20223
> ttl c
(integer) 16
> persist c
(integer) 1
> ttl c
(integer) -1

```

3. 字符串










