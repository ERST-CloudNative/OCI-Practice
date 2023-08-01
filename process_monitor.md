


根据需要，禁用操作系统防火墙

```
[root@monitor-processes ~] systemctl disable firewalld
[root@monitor-processes ~] systemctl stop firewalld
```

安装pushgateway

```
[root@monitor-processes ~] wget https://github.com/prometheus/pushgateway/releases/download/v0.8.0/pushgateway-0.8.0.linux-amd64.tar.gz
[root@monitor-processes ~] tar xvzf pushgateway-0.8.0.linux-amd64.tar.gz
[root@monitor-processes ~] cd pushgateway-0.8.0.linux-amd64/
[root@monitor-processes pushgateway-0.8.0.linux-amd64]# ./pushgateway &
```

安装prometheus

```
[root@monitor-processes ~] wget https://github.com/prometheus/prometheus/releases/download/v2.9.2/prometheus-2.9.2.linux-amd64.tar.gz
[root@monitor-processes ~] tar xvzf prometheus-2.9.2.linux-amd64.tar.gz
[root@monitor-processes ~] cd prometheus-2.9.2.linux-amd64/
[root@monitor-processes prometheus-2.9.2.linux-amd64]# cat prometheus.yml
# my global config
global:
  scrape_interval:     1s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090', 'localhost:9091']

[root@monitor-processes prometheus-2.9.2.linux-amd64]# ./prometheus &
```

安装Grafana

```
[root@monitor-processes ~]# yum install -y https://dl.grafana.com/oss/release/grafana-9.5.0-1.x86_64.rpm
[root@monitor-processes ~]# systemctl status grafana-server
[root@monitor-processes ~]# systemctl enable grafana-server --now
[root@monitor-processes ~]# systemctl status grafana-server

[root@monitor-processes ~]# echo "some_metric 3.14" | curl --data-binary @- http://pushgateway.example.org:9091/metrics/job/some_job
```

在目标主机上部署监控进程CPU使用情况的采集程序

```
[root@bg001 ~]# cat /opt/better-top
#!/bin/bash

while sleep 1

do
  input="/tmp/process-monitor.txt"
  output="/tmp/process-monitor-ret.txt"
  ps aux | awk 'NR>2{print line}{line=$0}' > $input
  cat $input | awk '{print "cpu_usage{process=\""$11"\", pid=\""$2"\"}", $3z}' > $output
  cat $output | curl --data-binary @-  http://152.69.224.148:9091/metrics/job/top/instance/machine
done

[root@bg001 ~]# chmod u+x /opt/better-top

[root@bg001 ~]# cat /etc/systemd/system/script_daemon.service
[Unit]
Description=Script Daemon

[Service]
Type=simple
ExecStart=/opt/better-top
Restart=on-failure

[Install]
WantedBy=default.target

```


访问Grafana：

<img width="955" alt="1690883515907" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/cafd38d1-76e1-40ce-9bff-a39ed89cb28e">

访问Prometheus：

<img width="638" alt="1690883605300" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e607bec1-244f-4f09-a809-b5715819232d">





