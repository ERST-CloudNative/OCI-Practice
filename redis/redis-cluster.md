
## Redis集群

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/30d8732b-692a-4e65-94f7-26554804e835)



开通OCI防火墙

```
10.0.0.0/24	All Protocols				All traffic for all ports
```

安装和配置redis服务

```
[root@rc-0x ~]# systemctl stop firewalld;systemctl disable firewalld
[root@rc-0x ~]# vim /etc/hosts

10.0.0.32 rc-01
10.0.0.40 rc-02
10.0.0.42 rc-03

[root@rc-0x ~]# wget https://download.redis.io/releases/redis-6.2.1.tar.gz
[root@rc-0x ~]# tar -zxvf redis-6.2.1.tar.gz -C /usr/local/redis_cluster/
[root@rc-0x ~]# cd /usr/local/redis_cluster/redis-6.2.1/;make && make install
[root@rc-0x ~]# cd src/;cp redis-server /usr/bin/;cp redis-cli /usr/bin/;cp redis-trib.rb /usr/bin/
[root@rc-0x ~]# vi /usr/local/redis_cluster/redis_6379/conf/redis.cnf

# 守护进行模式启动
daemonize yes

# 设置数据库数量，默认数据库为0
databases 16

# 绑定地址，需要修改
bind 10.0.0.42

# 绑定端口，需要修改
port 6379

# pid文件存储位置，文件名需要修改
pidfile /usr/local/redis_cluster/redis_6379/pid/redis_6379.pid

# log文件存储位置，文件名需要修改
logfile /usr/local/redis_cluster/redis_6379/logs/redis_6379.log

# RDB快照备份文件名，文件名需要修改
dbfilename redis_6379.rdb

# 本地数据库存储目录，需要修改
dir /usr/local/redis_cluster/redis_6379

# 集群相关配置
# 是否以集群模式启动
cluster-enabled yes

# 集群节点回应最长时间，超过该时间被认为下线
cluster-node-timeout 15000

# 生成的集群节点配置文件名，文件名需要修改
cluster-config-file nodes_6379.conf


[root@rc-0x ~]# vi /usr/local/redis_cluster/redis_6380/conf/redis.cnf

# 守护进行模式启动
daemonize yes

# 设置数据库数量，默认数据库为0
databases 16

# 绑定地址，需要修改
bind 10.0.0.42

# 绑定端口，需要修改
port 6380

# pid文件存储位置，文件名需要修改
pidfile /usr/local/redis_cluster/redis_6380/pid/redis_6380.pid

# log文件存储位置，文件名需要修改
logfile /usr/local/redis_cluster/redis_6380/logs/redis_6380.log

# RDB快照备份文件名，文件名需要修改
dbfilename redis_6380.rdb

# 本地数据库存储目录，需要修改
dir /usr/local/redis_cluster/redis_6380

# 集群相关配置
# 是否以集群模式启动
cluster-enabled yes

# 集群节点回应最长时间，超过该时间被认为下线
cluster-node-timeout 15000

# 生成的集群节点配置文件名，文件名需要修改
cluster-config-file nodes_6380.conf

[root@rc-0x ~]# redis-server /usr/local/redis_cluster/redis_6379/conf/redis.cnf;redis-server /usr/local/redis_cluster/redis_6380/conf/redis.cnf

```

组件集群

```
[root@rc-01 ~]# redis-cli -h rc-01 -p 6379
rc-01:6379> cluster meet 10.0.0.32 6380
OK
rc-01:6379> cluster meet 10.0.0.40 6379
OK
rc-01:6379> cluster meet 10.0.0.40 6380
OK
rc-01:6379> cluster meet 10.0.0.42 6379
OK
rc-01:6379> cluster meet 10.0.0.42 6380
OK
rc-01:6379> cluster nodes
3feec50ef280bfe47eec61243d8cd15dc313459e 10.0.0.42:6379@16379 master - 0 1700634357317 4 connected
30a8c402f45a75395aea8f61bb6b4ffe65f9168a 10.0.0.42:6380@16380 master - 0 1700634357000 5 connected
c18b3fc255252a615771e22b81d405572db466a3 10.0.0.40:6380@16380 master - 0 1700634356315 3 connected
6fc9216646c9e0a9c5e8a991efb1eafd5334f18d 10.0.0.32:6379@16379 myself,master - 0 1700634356000 2 connected
63515f48af3cb6147120373306c79e4313215786 10.0.0.32:6380@16380 master - 0 1700634356000 1 connected
ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 10.0.0.40:6379@16379 master - 0 1700634355314 0 connected
rc-01:6379> exit

```

配置主从复制关系

```
[root@rc-01 ~]# redis-cli -h rc-01 -p 6380
rc-01:6380> cluster replicate ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6
OK
rc-01:6380> exit
[root@rc-01 ~]# redis-cli -h rc-02 -p 6380
rc-02:6380> cluster replicate 3feec50ef280bfe47eec61243d8cd15dc313459e
OK
rc-02:6380> exit
[root@rc-01 ~]# redis-cli -h rc-03 -p 6380
rc-03:6380> cluster replicate 6fc9216646c9e0a9c5e8a991efb1eafd5334f18d
OK
rc-03:6380> exit

```

分配槽位

```
[root@rc-01 ~]# redis-cli -h rc-01 -p 6379 cluster addslots {0..5461}
OK
[root@rc-01 ~]# redis-cli -h rc-02 -p 6379 cluster addslots {5462..10922}
OK
[root@rc-01 ~]# redis-cli -h rc-03 -p 6379 cluster addslots {10923..16383}
OK
[root@rc-01 ~]#
[root@rc-01 ~]#
[root@rc-01 ~]# redis-cli -h rc-01 -p 6379
rc-01:6379> cluster nodes
3feec50ef280bfe47eec61243d8cd15dc313459e 10.0.0.42:6379@16379 master - 0 1700635646000 4 connected 10923-16383
30a8c402f45a75395aea8f61bb6b4ffe65f9168a 10.0.0.42:6380@16380 slave 6fc9216646c9e0a9c5e8a991efb1eafd5334f18d 0 1700635647000 2 connected
c18b3fc255252a615771e22b81d405572db466a3 10.0.0.40:6380@16380 slave 3feec50ef280bfe47eec61243d8cd15dc313459e 0 1700635647888 4 connected
6fc9216646c9e0a9c5e8a991efb1eafd5334f18d 10.0.0.32:6379@16379 myself,master - 0 1700635645000 2 connected 0-5461
63515f48af3cb6147120373306c79e4313215786 10.0.0.32:6380@16380 slave ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 0 1700635646887 0 connected
ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 10.0.0.40:6379@16379 master - 0 1700635647000 0 connected 5462-10922

rc-01:6379> CLUSTER info
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:6
cluster_size:3
cluster_current_epoch:5
cluster_my_epoch:2
cluster_stats_messages_ping_sent:1666
cluster_stats_messages_pong_sent:1589
cluster_stats_messages_meet_sent:5
cluster_stats_messages_sent:3260
cluster_stats_messages_ping_received:1589
cluster_stats_messages_pong_received:1671
cluster_stats_messages_received:3260

```

尝试写入

```
rc-01:6379> set k1 v1
(error) MOVED 12706 10.0.0.42:6379
rc-01:6379> exit
```
如何解决这个问题？其实在登录的时候加上参数-c即可，-c参数无所谓你的Redis是否是集群模式，建议任何登录操作都加上，这样即使是Redis集群也会自动进行MOVED重定向：

```
[root@rc-01 ~]# redis-cli -c -h rc-01 -p 6379
rc-01:6379> set k1 v1
-> Redirected to slot [12706] located at 10.0.0.42:6379
OK

```

验证主从复制是否生效

```
[root@rc-02 ~]# redis-cli -h rc-02 -p 6380
rc-02:6380> keys *
1) "k1"

```

故障转移验证

```
# 模拟故障
[root@rc-01 ~]# redis-cli -h rc-01 -p 6379 shutdown

# 查看集群节点情况，可以发现原来的节点已经下线，新的master节点上线(原来是先前的slave节点)
[root@rc-01 ~]# redis-cli -c -h rc-02 -p 6379
rc-02:6379> cluster nodes
ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 10.0.0.40:6379@16379 myself,master - 0 1700639611000 0 connected 5462-10922
6fc9216646c9e0a9c5e8a991efb1eafd5334f18d 10.0.0.32:6379@16379 master,fail - 1700639591950 1700639588000 2 disconnected
63515f48af3cb6147120373306c79e4313215786 10.0.0.32:6380@16380 slave ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 0 1700639612969 0 connected
3feec50ef280bfe47eec61243d8cd15dc313459e 10.0.0.42:6379@16379 master - 0 1700639607964 4 connected 10923-16383
c18b3fc255252a615771e22b81d405572db466a3 10.0.0.40:6380@16380 slave 3feec50ef280bfe47eec61243d8cd15dc313459e 0 1700639611968 4 connected
30a8c402f45a75395aea8f61bb6b4ffe65f9168a 10.0.0.42:6380@16380 master - 0 1700639610968 6 connected 0-5461

# 故障恢复
[root@rc-01 ~]# redis-server /usr/local/redis_cluster/redis_6379/conf/redis.cnf

# 先前的master节点则作为slave节点
[root@rc-01 ~]# redis-cli -c -h rc-01 -p 6379
rc-01:6379> cluster nodes
3feec50ef280bfe47eec61243d8cd15dc313459e 10.0.0.42:6379@16379 master - 0 1700639790769 4 connected 10923-16383
6fc9216646c9e0a9c5e8a991efb1eafd5334f18d 10.0.0.32:6379@16379 myself,slave 30a8c402f45a75395aea8f61bb6b4ffe65f9168a 0 1700639788000 6 connected
c18b3fc255252a615771e22b81d405572db466a3 10.0.0.40:6380@16380 slave 3feec50ef280bfe47eec61243d8cd15dc313459e 0 1700639790000 4 connected
30a8c402f45a75395aea8f61bb6b4ffe65f9168a 10.0.0.42:6380@16380 master - 0 1700639791771 6 connected 0-5461
ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 10.0.0.40:6379@16379 master - 0 1700639790000 0 connected 5462-10922
63515f48af3cb6147120373306c79e4313215786 10.0.0.32:6380@16380 slave ec2d24f4ed1d1900e629e51c34fd2ebd49d123a6 0 1700639789000 0 connected

```


