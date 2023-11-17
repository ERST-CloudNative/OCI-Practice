## Redis中执行Lua脚本

这里主要分为两部分：
1. 如何在Redis中执行Lua脚本
2. 如何在Redis中禁用eval功能

### 1. 在Redis中执行Lua脚本

```
# 安装redis
[root@redis01 ~]# dnf install epel-release
[root@redis01 ~]# dnf install redis
[root@redis01 ~]# systemctl start redis
[root@redis01 ~]# redis-cli ping
PONG

# 在命令行中执行lua脚本
[root@redis01 ~]# redis-cli
127.0.0.1:6379> EVAL "local current = redis.call('GET', KEYS[1]) if current then redis.call('SET', KEYS[1], tonumber(current) + 1) else redis.call('SET', KEYS[1], 1) end return redis.call('GET', KEYS[1])" 1 mykey
"1"
127.0.0.1:6379>
127.0.0.1:6379> keys *
1) "mykey"
127.0.0.1:6379> get mykey
"1"
```

### 2. 如何在Redis中禁用eval功能

由于eval 功能的灵活性和强大性，使得它也成为了一种潜在的安全隐患。如果不加限制地允许用户执行任意的 Lua 脚本，那么可能会导致 Redis 服务器被入侵、数据库被破坏等安全问题。因此，禁用 Redis 中 eval 功能是一种有效的安全防护措施。

```
[root@redis01 ~]# vi /etc/redis.conf

# 新增以下一行配置即可
...
rename-command eval ""
...

[root@redis01 ~]# systemctl restart redis

[root@redis01 ~]# redis-cli
127.0.0.1:6379> EVAL "local current = redis.call('GET', KEYS[1]) if current then redis.call('SET', KEYS[1], tonumber(current) + 1) else redis.call('SET', KEYS[1], 1) end return redis.call('GET', KEYS[1])" 1 mykey
(error) ERR unknown command `EVAL`, with args beginning with: `local current = redis.call('GET', KEYS[1]) if current then redis.call('SET', KEYS[1], tonumber(current) + 1) else redis.call('SE`,

```
