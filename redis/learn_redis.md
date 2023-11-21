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

7. 有序集合

Redis 有序集合和集合一样也是 string 类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个 double 类型的分数。redis 正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数(score)却可以重复。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。 集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

```
# 向有序集合添加一个或多个成员，或者更新已存在成员的分数
> zadd z1 1 redis
(integer) 1
> zadd z1 2 mongodb
(integer) 1
> zadd z1 3 mysql
(integer) 1
> zadd z1 3 mysql
(integer) 0
> zadd z1 4 mysql
(integer) 0
> zadd z1 3 pgsql
(integer) 1

# 通过索引区间返回有序集合指定区间内的成员
> zrange z1 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "pgsql"
6) "3"
7) "mysql"
8) "4"


> zadd z2 1 redis
(integer) 1
> zadd z2 2 mongodb
(integer) 1
> zadd z2 3 mysql
(integer) 1
> zrange z2 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "mysql"
6) "3"
> zadd z2 4 mysql
(integer) 0
> zrange z2 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "mysql"
6) "4"

# 获取有序集合的成员数
> zcard z1
(integer) 4

# 计算在有序集合中指定区间分数的成员数
> zcount z1 2 4
(integer) 3
> zrange z1 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "pgsql"
6) "3"
7) "mysql"
8) "4"

# 有序集合中对指定成员的分数加上增量 increment
> zincrby z1 2 "pgsql"
"5"
> zrange z1 0 10 withscores
1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "mysql"
6) "4"
7) "pgsql"
8) "5"

# 对于一个所有成员的分值都相同的有序集合键key来说，这个命令会返回该集合中，成员介于min和max范围内的元素数量
> zlexcount z1 - +
(integer) 4
> zadd test10 0 apple
(integer) 1
> zadd test10 0 redis
(integer) 1
> zadd test10 0 org
(integer) 1
> zadd test10 0 zoo
(integer) 1
> zlexcount test10 "[a" "[z"
(integer) 3
> zlexcount test10 "[a" "[zoo"
(integer) 4
> zlexcount test10 "[b" "[zoo"
(integer) 3
> zlexcount test10 "[o" "[zoo"
(integer) 3
> zlexcount test10 "[oz" "[zoo"
(integer) 2


> zrange  z1 2 4
1) "mysql"
2) "pgsql"

# 返回有序集合中指定成员的索引
> zrank z1 mysql
(integer) 2
> zrange z1 0 10
1) "redis"
2) "mongodb"
3) "mysql"
4) "pgsql"

# 移除有序集合中的一个或多个成员
> zrem z1 mysql
(integer) 1
> zrange z1 0 10
1) "redis"
2) "mongodb"
3) "pgsql"

# 返回有序集中指定区间内的成员，通过索引，分数从高到低
> zrevrange z1 0 10
1) "pgsql"
2) "mongodb"
3) "redis"

# 返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序
> zrevrank z1 redis
(integer) 2

# 迭代有序集合中的元素（包括元素成员和元素分值）
> zscan z1 0 match "r*"
1) "0"
2) 1) "redis"
   2) "1"


```

8. HyperLogLog

HyperLogLog 主要的应用场景就是进行基数统计。这个问题的应用场景其实是十分广泛的。例如：对于 Google 主页面而言，同一个账户可能会访问 Google 主页面多次。于是，在诸多的访问流水中，如何计算出 Google 主页面每天被多少个不同的账户访问过就是一个重要的问题。那么对于 Google 这种访问量巨大的网页而言，其实统计出有十亿 的访问量或者十亿零十万的访问量其实是没有太多的区别的，因此，在这种业务场景下，为了节省成本，其实可以只计算出一个大概的值，而没有必要计算出精准的值。

对于上面的场景，可以使用HashMap、BitMap和HyperLogLog来解决。对于这三种解决方案，这边做下对比：

HashMap：算法简单，统计精度高，对于少量数据建议使用，但是对于大量的数据会占用很大内存空间；
BitMap：位图算法，具体内容可以参考我的这篇文章，统计精度高，虽然内存占用要比HashMap少，但是对于大量数据还是会占用较大内存；
HyperLogLog：存在一定误差，占用内存少，稳定占用 12k 左右内存，可以统计 2^64 个元素，对于上面举例的应用场景，建议使用。


什么是基数?
比如数据集 {1, 3, 5, 7, 5, 7, 8, 9}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8, 9}, 基数(不重复元素)为6。 基数估计就是在误差可接受的范围内，快速计算基数。

```
> pfadd demo redis mongodb mysql
(integer) 1
> PFCOUNT demo
(integer) 3
> pfadd demo redis
(integer) 0
> PFCOUNT demo
(integer) 3
> pfadd demo redis  1 2 3 4 5
(integer) 1
> PFCOUNT demo
(integer) 8

```

9. 发布订阅

Redis 发布订阅 (pub/sub) 是一种消息通信模式：发送者 (pub) 发送消息，订阅者 (sub) 接收消息。

Redis 客户端可以订阅任意数量的频道。

下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/916aa23d-a613-4267-b63c-c1aa46321f09)

当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6ad2018e-22d0-4763-b8df-7b55990bdf0d)


```
> SUBSCRIBE runoobChat
1) "subscribe"
2) "runoobChat"
3) (integer) 1
1) "message"
2) "runoobChat"
3) "Redis PUBLISH test"
1) "message"
2) "runoobChat"
3) "Hello Loren"
(subscribed mode)>
1) "message"
2) "runoobChat"
3) "Hello world"
(subscribed mode)> UNSUBSCRIBE runoobChat
1) "unsubscribe"
2) "runoobChat"
3) (integer) 0

```

```
> PUBLISH runoobChat "Redis PUBLISH test"
(integer) 1
> PUBLISH runoobChat "Hello Loren"
(integer) 1
> PUBLISH runoobChat "Hello world"
(integer) 1
> PUBLISH runoobChat "Hello world2"
(integer) 0
```

10. Redis 事务

Redis 事务可以一次执行多个命令， 并且带有以下三个重要的保证：

- 批量操作在发送 EXEC 命令前被放入队列缓存。
- 收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
- 在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。

一个事务从开始到执行会经历以下三个阶段：
- 开始事务。
- 命令入队。
- 执行事务。

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。
事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。

```
# 开启事务
> multi
OK
(TX)> SET book-name "Mastering C++ in 21 days"
QUEUED
(TX)> GET book-name
QUEUED
(TX)> SADD tag "C++" "Programming" "Mastering Series"
QUEUED
(TX)> SMEMBERS tag
QUEUED
# 执行事务
(TX)> exec
1) OK
2) "Mastering C++ in 21 days"
3) (integer) 3
4) 1) "C++"
   2) "Programming"
   3) "Mastering Series"

> multi
OK
(TX)> set ac 123
QUEUED
(TX)> discard
OK
> set a11 188
OK
> multi
OK
# 取消事务
(TX)> discard
OK

# 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。
> watch a11
OK
> multi
OK
(TX)> set a11 199
QUEUED
(TX)> get a11
QUEUED
(TX)> set a12 100
QUEUED
# 事务被打断
(TX)> exec
(nil)
> get a11
"200"

# 取消 WATCH 命令对所有 key 的监视。
> unwatch
OK

```

```
> set a11 200
OK

```

11. redis连接

```
# 配置密码
[root@redis01 ~]# vi /etc/redis.conf
...
requirepass 1qaz2wsx
...

[root@redis01 ~]# systemctl restart redis

[root@redis01 ~]# redis-cli
127.0.0.1:6379> set a 123
(error) NOAUTH Authentication required.
# 验证密码
127.0.0.1:6379> auth 1qaz2wsx
OK
127.0.0.1:6379> set a 123
OK

```

12. redis服务配置

获取redis服务信息，详细的命令行在后面的内容逐步展开。

```
127.0.0.1:6379> select 1
OK
127.0.0.1:6379[1]> set a 123
OK
127.0.0.1:6379[1]> select 0
OK
127.0.0.1:6379> info
# Server
redis_version:5.0.3
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:d76aa7e3f6a5cce1
redis_mode:standalone
os:Linux 5.15.0-105.125.6.2.1.el8uek.x86_64 x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:8.4.1
process_id:48192
run_id:d21d363760877e176bafdb304631acc88130aa8e
tcp_port:6379
uptime_in_seconds:351513
uptime_in_days:4
hz:10
configured_hz:10
lru_clock:6058990
executable:/usr/bin/redis-server
config_file:/etc/redis.conf

# Clients
connected_clients:1
client_recent_max_input_buffer:2
client_recent_max_output_buffer:0
blocked_clients:0

# Memory
used_memory:854072
used_memory_human:834.05K
used_memory_rss:10653696
used_memory_rss_human:10.16M
used_memory_peak:854072
used_memory_peak_human:834.05K
used_memory_peak_perc:100.01%
used_memory_overhead:840894
used_memory_startup:790984
used_memory_dataset:13178
used_memory_dataset_perc:20.89%
allocator_allocated:914920
allocator_active:1114112
allocator_resident:3948544
total_system_memory:8007581696
total_system_memory_human:7.46G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.22
allocator_frag_bytes:199192
allocator_rss_ratio:3.54
allocator_rss_bytes:2834432
rss_overhead_ratio:2.70
rss_overhead_bytes:6705152
mem_fragmentation_ratio:13.12
mem_fragmentation_bytes:9841616
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:49694
mem_aof_buffer:0
mem_allocator:jemalloc-5.1.0
active_defrag_running:0
lazyfree_pending_objects:0

# Persistence
loading:0
rdb_changes_since_last_save:1
rdb_bgsave_in_progress:0
rdb_last_save_time:1700557704
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:147456
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0

# Stats
total_connections_received:3
total_commands_processed:8
instantaneous_ops_per_sec:0
total_net_input_bytes:310
total_net_output_bytes:3560
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:274
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0

# Replication
role:master
connected_slaves:0
master_replid:cacbc3d5243f46fee973e5d5cea2cc4e23067780
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:131.861209
used_cpu_user:89.863490
used_cpu_sys_children:0.001623
used_cpu_user_children:0.000000

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=2,expires=0,avg_ttl=0
db1:keys=1,expires=0,avg_ttl=0


```

