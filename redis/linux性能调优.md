## 性能调优

当面对高并发场景时，文件句柄数和网络配置是关键的优化点。以下是进一步丰富的配置说明：

1. 文件描述符限制：

配置文件： /etc/security/limits.conf

```
*       soft    nofile  65536
*       hard    nofile  65536
```
作用： 提高系统对文件描述符的限制，以适应高并发场景中可能存在的大量连接和文件句柄需求。

配置文件： /etc/sysctl.conf

```
fs.file-max = 65536
```
作用： 提高系统的最大文件数限制，确保足够的文件描述符可供使用。

2. 网络参数调整：

配置文件： /etc/sysctl.conf

```
net.core.somaxconn = 65536
net.ipv4.tcp_max_syn_backlog = 65536
net.core.netdev_max_backlog = 65536
```

作用：
net.core.somaxconn: 增加同时处于半连接状态的最大数量，适用于高连接率场景。
net.ipv4.tcp_max_syn_backlog: 增加TCP握手队列的最大长度，适用于处理大量短连接请求。
net.core.netdev_max_backlog: 增加网络设备接收数据包的最大排队长度，防止丢包。

```
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 87380 16777216
net.ipv4.tcp_mem = 50576 64768 98152
net.ipv4.tcp_max_tw_buckets = 6000
net.ipv4.tcp_fin_timeout = 30
```

作用：

net.core.rmem_max 和 net.core.wmem_max: 设置单个套接字接收和发送缓冲区的最大值。
net.ipv4.tcp_rmem 和 net.ipv4.tcp_wmem: 设置TCP套接字接收和发送缓冲区的最小、默认、最大值。
net.ipv4.tcp_mem: 设置TCP栈的内存分配策略。
net.ipv4.tcp_max_tw_buckets: 设置TIME-WAIT套接字的最大数量，避免过多的TIME-WAIT连接。
net.ipv4.tcp_fin_timeout: 设置TCP连接的最大存活时间。


```
net.ipv4.tcp_fastopen = 3
```
作用： 开启TCP快速打开，加速TCP连接的建立过程。


```
net.core.default_qdisc = fq
net.ipv4.tcp_congestion_control = bbr
```

作用： 使用TCP BBR拥塞控制算法，提高网络拥塞控制的效率。


3. 关闭透明大页（Transparent Huge Pages）：

编辑 /etc/rc.d/rc.local 文件，在文件末尾添加以下命令：

```
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```
运行以下命令使配置生效：

```
chmod +x /etc/rc.d/rc.local
systemctl enable rc-local
systemctl start rc-local

```

> 在高并发的数据库系统中，例如Redis，关闭透明大页通常是为了避免潜在的性能问题。

```
在Redis服务器上关闭透明大页（Transparent Huge Pages）的主要原因是避免性能问题。透明大页是一种操作系统级别的内存管理技术，它将连续的小页（通常是4KB）合并成更大的页面（通常是2MB或1GB），以提高内存的利用率。然而，在某些情况下，透明大页可能导致性能下降，特别是对于需要快速随机访问内存的应用程序，如Redis。

以下是关闭透明大页的一些原因：
- 内存分配的不连续性： 透明大页的合并操作可能导致内存分配的不连续性，使得分配大块连续内存变得更加困难。对于Redis这样的内存密集型应用，需要频繁地进行内存分配和释放，这可能导致性能下降。
- TLB失效： 透明大页的使用可能导致Translation Lookaside Buffer（TLB）失效的增加。TLB是CPU用于加速虚拟地址到物理地址映射的缓存，而透明大页的使用可能导致TLB失效的频繁发生，从而影响内存访问的速度。
- 长时间回收操作： 透明大页的回收操作可能需要较长的时间，这可能导致系统在进行内存回收时产生的延迟。对于实时性要求较高的应用，如缓存系统，这可能会对性能产生负面影响。

在Redis等内存密集型应用中，这些问题可能会显著影响性能。因此，关闭透明大页可以是一种优化选项，以确保更可预测且稳定的性能。
```
