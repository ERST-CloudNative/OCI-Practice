## Opensearch 尝试配置记录


创建用户组

<img width="660" alt="1685090355074" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d9d892ee-4030-4292-985a-14b08193a4b3">


创建`policy`

```
Allow group opensearch-group to manage opensearch-family in compartment demo
Allow service opensearch to manage vcns in compartment demo
Allow service opensearch to manage vnics in compartment demo
Allow service opensearch to use subnets in compartment demo
Allow service opensearch to use network-security-groups in compartment demo
```

获取用户名密码的Base64加密文本

```
[root@opensearch-test ~]# curl -v -u USER_NAME:PASSWORD  http://[NGINX_HOST_IP]:8080/app/home

> Authorization: Basic [Your base64]


```

NginX配置参考，可以在此基础上添加用户认证、TLS等。

```

[root@opensearch-test ~]# cat /etc/nginx/nginx.conf
user root;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /var/run/nginx.pid;

include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen 8080;
        server_name _;

        location / {
        # Host should be OCI OpenSearch Dashboard API Endpoint
        proxy_set_header Host https://[ABC].opendashboard.ap-tokyo-1.oci.oraclecloud.com:5601;
        # Compute Instance IP
        proxy_set_header X-Real-IP 【NGINX-HOST_IP】;
        # Various headers
        proxy_http_version 1.1;
        proxy_set_header Connection "Keep-Alive";
        proxy_set_header Proxy-Connection "Keep-Alive";
        proxy_set_header Authorization "Basic [ABC]";
        # Forward requests to OpenSearch Dashboard API.
        proxy_pass https://[ABC].opendashboard.ap-tokyo-1.oci.oraclecloud.com:5601;
        }

        location /app/home {
        # Set Host to match ES endpoint
        proxy_set_header Host https://[ABC].opensearch.ap-tokyo-1.oci.oraclecloud.com:9200;
        # We want to be sure that we are sending instance IP instead of browser's IP
        proxy_set_header X-Real-IP 【NGINX-HOST_IP】;

        # Various headers
        proxy_http_version 1.1;
        proxy_set_header Connection "Keep-Alive";
        proxy_set_header Proxy-Connection "Keep-Alive";
        proxy_set_header Authorization "Basic [ABC]";

        # Forward requests to OCI OpenSearch Dashboard API
        proxy_pass https://[ABC].opendashboard.ap-tokyo-1.oci.oraclecloud.com:5601/app/home;

        # Ensure that requests are coming back to /app/home
        proxy_redirect https://[ABC].opendashboard.ap-tokyo-1.oci.oraclecloud.com:5601/app/home http://【NGINX-HOST_IP】:8080/app/home;
        }
    }

    server {
        listen 9200;
        server_name _;


        location / {
        # Host should be OCI OpenSearch API Endpoint
        proxy_set_header Host https://[ABC].opensearch.ap-tokyo-1.oci.oraclecloud.com:9200;
        proxy_set_header X-Real-IP 【NGINX-HOST_IP】;


        # Various headers
        proxy_http_version 1.1;
        proxy_set_header Connection "Keep-Alive";
        proxy_set_header Authorization "Basic XXXXXXX";
        # Forward requests to OCI OpenSearch API
        proxy_pass https://[ABC].opensearch.ap-tokyo-1.oci.oraclecloud.com:9200;
        }
    }
}

```



```
[root@opensearch-test ~]# curl -H 'Content-Type: application/x-ndjson' -XPOST "http://[NGINX_HOST_IP]:9200/oci/_bulk?pretty" --data-binary @OCI_services.json

[root@opensearch-test ~]# curl "http://[NGINX_HOST_IP]:9200/_cat/indices"
green  open oci_metrics  HagwvgySSfK_IdZVcdIP2g 1 0 15160 15059  1.9mb  1.9mb
yellow open oci          V1t9cp15R3mOwU5-Ae1pww 1 1    54     0 50.7kb 50.7kb
green  open oci_security c8Fh9RNLRpWe6ek12RjK9w 1 0     9     3 32.3kb 32.3kb
green  open oci_ilm      Jar21LNgQUGOWviQ7yErZA 1 0     1     0  8.6kb  8.6kb
green  open .kibana_1    J6ISm3AQS9OoFicFBlpgdQ 1 0     1     0  5.2kb  5.2kb

[root@opensearch-test ~]# curl -X GET "http://[NGINX_HOST_IP]:9200/oci/_search?q=title:Kubernetes&pretty"
{
  "took" : 14,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 2.6731052,
    "hits" : [
      {
        "_index" : "oci",
        "_id" : "10",
        "_score" : 2.6731052,
        "_source" : {
          "id" : 10,
          "title" : "Oracle Container Engine for Kubernetes",
          "category" : "Compute",
          "url" : "https://www.oracle.com/cloud-native/container-engine-kubernetes/",
          "text" : "Oracle Container Engine for Kubernetes is an Oracle-managed container orchestration service that can reduce the time and cost to build modern cloud native applications. Unlike most other vendors, Oracle Cloud Infrastructure provides Container Engine for Kubernetes as a free service that runs on higher-performance, lower-cost compute shapes. DevOps engineers can use unmodified, open source Kubernetes for application workload portability and to simplify operations with automatic updates and patching."
        }
      }
    ]
  }
}

```
























