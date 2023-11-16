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

```
> set ab 123456
OK

# 获取长度
> strlen ab
(integer) 6
> set cnt 12
OK
# 对整数型字符串自增
> incr cnt
(integer) 13
> incr cnt
(integer) 14
> get cnt
"14"
# 对整数型字符串自减
> decr cnt
(integer) 13
> decr cnt
(integer) 12
> get cnt
"12"

# 对整数型字符串自增，步长为2
> incrby cnt 2
(integer) 14
> incrby cnt 3
(integer) 17
> get cnt
"17"

# 对整数型字符串自减，步长为3
> decrby cnt 3
(integer) 14
> decrby cnt 2
(integer) 12
> get cnt
"12"
> set a1 2
OK

# 添加字符串
> append a1 3
(integer) 2
> get a1
"23"

# 同时获取多个键值
> mget a1 cnt
1) "23"
2) "12"

# 设置键值，并返回上一次的值
> getset a1 66
"23"

> set b1 1234567890
OK
# 获取字符串数组的指定序列
> getrange b1 1 5
"23456"

```

4. 哈希

```
# 单个字段哈希键值
> hset oci name "oracle cloud infra"
(integer) 1

> hget oci name
"oracle cloud infra"

# 多个字段哈希键值
> hmset h1 name "news"  descriptions "good news" likes 20 vistors 10000
OK
> hgetall h1
1) "name"
2) "news"
3) "descriptions"
4) "good news"
5) "likes"
6) "20"
7) "vistors"
8) "10000"

# 检查字段是否存在
> HEXISTS h1 name
(integer) 1
> HEXISTS h1 likes
(integer) 1

# 删除字段
> hdel h1 likes
(integer) 1
> hgetall h1
1) "name"
2) "news"
3) "descriptions"
4) "good news"
5) "vistors"
6) "10000"

# 获取哈希表中的所有字段
> hkeys h1
1) "name"
2) "descriptions"
3) "vistors"

# 获取哈希表的长度
> hlen h1
(integer) 3

# 获取哈希表中指定字段的值
> hmget h1 name vistors
1) "news"
2) "10000"

# 设置字段
> hsetnx h1 likes 200
(integer) 1
> hkeys h1
1) "name"
2) "descriptions"
3) "vistors"
4) "likes"

# 迭代哈希表中的键值对，默认从0开始。
> hscan h1 0
1) "0"
2) 1) "name"
   2) "news"
   3) "descriptions"
   4) "good news"
   5) "vistors"
   6) "10000"
   7) "likes"
   8) "200"

# 返回指定模式匹配的字段
> hscan h1 0 match "n*"
1) "0"
2) 1) "name"
   2) "news"
```


5. 列表

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

```
# 添加元素到列表
> lpush mid redis
(integer) 1
> lpush mid mongodb
(integer) 2
> lpush mid mysql
(integer) 3

# 获取列表指定范围内的元素
> lrange mid 0 10
1) "mysql"
2) "mongodb"
3) "redis"

# 移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
> blpop mid 3
1) "mid"
2) "mysql"

# 通过索引获取列表中的元素
> lindex mid 0
"mongodb"
> lindex mid 1
"redis"

# 在列表的元素前或者后插入元素
> linsert mid before redis pgsql
(integer) 3
> lrange mid 0 10
1) "mongodb"
2) "pgsql"
3) "redis"
> lindex mid 0
"mongodb"
> lindex mid 1
"pgsql"
> lindex mid 2
"redis"
> llen mid
(integer) 3

# 通过索引设置列表元素的值
> lset mid 1 postgresql
OK
> lrange mid 0 10
1) "mongodb"
2) "postgresql"
3) "redis"

# 移除列表的最后一个元素，返回值为移除的元素。
> rpop mid
"redis"
> lrange mid 0 10
1) "mongodb"
2) "postgresql"

# 在列表中添加一个或多个值到列表尾部
> rpush mid docker k8s
(integer) 4
> lrange mid 0 10
1) "mongodb"
2) "postgresql"
3) "docker"
4) "k8s"

```

6. 集合

Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

集合对象的编码可以是 intset 或者 hashtable。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

```
# 向集合添加一个或多个成员
> sadd s1 redis
(integer) 1
> sadd s1 mogodb
(integer) 1
> sadd s1 mysql
(integer) 1
> sadd s1 mysql
(integer) 0

# 返回集合中的所有成员
> smembers s1
1) "mogodb"
2) "mysql"
3) "redis"

# 获取集合的成员数
> scard s1
(integer) 3


> sadd s2 redis
(integer) 1
> sadd s2 pgsql
(integer) 1
> sadd s2 docker
(integer) 1

# 返回第一个集合与其他集合之间的差异。
> sdiff s1 s2
1) "mogodb"
2) "mysql"

# 返回给定所有集合的交集
> sinter s1 s2
1) "redis"

# 判断 member 元素是否是集合 key 的成员
> sismember s1 redis
(integer) 1

# 移除并返回集合中的一个随机元素
> spop s1
"mogodb"
> smembers s1
1) "mysql"
2) "redis"

# 返回集合中一个或多个随机数
> srandmember s2
"redis"
> srandmember s2
"redis"
> srandmember s2
"docker"
> srandmember s2
"redis"

# 移除集合中一个或多个成员
> srem s1 mysql
(integer) 1
> smembers s1
1) "redis"

# 返回所有给定集合的并集
> sunion s1 s2
1) "pgsql"
2) "docker"
3) "redis"

# 迭代集合中的元素
> sscan s2 0
1) "0"
2) 1) "pgsql"
   2) "docker"
   3) "redis"
> sscan s2 0 match "d*"
1) "0"
2) 1) "docker"

```















