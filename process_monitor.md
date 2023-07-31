


```
    1  systemctl disable firewalld
    2  systemctl stop firewalld
    3  wget https://github.com/prometheus/pushgateway/releases/download/v0.8.0/pushgateway-0.8.0.linux-amd64.tar.gz
    4  ls
    5  tar xvzf pushgateway-0.8.0.linux-amd64.tar.gz
    6  cd pushgateway-0.8.0.linux-amd64/
    7  ls
    8  ./pushgateway &
    9  cd
   10  wget https://github.com/prometheus/prometheus/releases/download/v2.9.2/prometheus-2.9.2.linux -amd64.tar.gz
   11  tar xvzf prometheus-2.9.2.linux-amd64.tar.gz
   12  ls
   13  rm -f md64.tar.gz
   14  rm -f pushgateway-0.8.0.linux-amd64
   15  ls
   16  ps
   17  wget https://github.com/prometheus/prometheus/releases/download/v2.9.2/prometheus-2.9.2.linux-amd64.tar.gz
   18  tar xvzf prometheus-2.9.2.linux-amd64.tar.gz
   19  cd prometheus-2.9.2.linux-amd64/
   20  vi prometheus.yml
   21  ls
   22  ./prometheus &
   23  cd
   24  wget https://dl.grafana.com/oss/release/grafana_6.2.0-beta1_amd64.deb; dpkg -i grafana_6.2.0-beta1_amd64.deb
   25  ls
   26  rm -f grafana_6.2.0-beta1_amd64.deb
   27  yum install -y https://dl.grafana.com/oss/release/grafana-9.5.0-1.x86_64.rpm
   28  systemctl status grafana
   29  systemctl status grafana-server
   30  systemctl enable grafana-server --now
   31  systemctl status grafana-server
   32  var="some_metric 3.14"
   33  curl -X POST -H  "Content-Type: text/plain" --data "$var" http://152.69.224.148:9091/metrics/job/top/instance/machine
   34  echo "some_metric 3.14" | curl --data-binary @- http://pushgateway.example.org:9091/metrics/job/some_job
   35  echo "some_metric 3.14" | curl --data-binary @- http://127.0.0.1:9091/metrics/job/some_job
   36  echo "some_metric 3.14" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   37  echo "cpu_usage{process="[kthreadd]", pid="2"} 0.0" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   38  echo "cpu_usage{process=\"[kthreadd]\", pid=\"2\"} 0.0" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   39  echo "cpu_usage{process=\"[kthreadd]\", pid=\"2\"} 0.0cpu_usage{process=\"[kthreadd]\", pid=\"3\"} 0.1" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   40  echo "cpu_usage{process=\"[kthreadd]\", pid=\"2\"} 0.0 cpu_usage{process=\"[kthreadd]\", pid=\"3\"} 0.1" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   41  echo "cpu_usage{process=\"[kthreadd]\", pid=\"2\"} 0.0\r\ncpu_usage{process=\"[kthreadd]\", pid=\"3\"} 0.1" | curl --data-binary @- http://152.69.224.148:9091/metrics/job/some_job
   42  ps aux
   43  history

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

```
