

### 环境说明：
- 2 台 NGINX
- 2 台 WEB(自行部署nginx或者httpd服务器，这里不做详述)
- 1 个私有IP，Assign Secondary Private IP Address,用作VIP

### 部署两台NGINX

#### 1. 安装NGINX\KeepAlived以及OCI命令行工具
```
[root@nginx0x ~]# yum install -y nginx keepalived
[root@nginx0x ~]# dnf -y install oraclelinux-developer-release-el8
[root@nginx0x ~]# dnf install python36-oci-cli

```

#### 2. 配置OCI，其中产生的oci_api_key_public.pem需要上传到用户的API KEY下

```
[root@nginx0x ~]# oci setup config
[root@nginx0x ~]# oci compute instance list --compartment-id ocid1.compartment.oc1..xxxxxxx
``

#### 3. 配置各个NGINX节点

NGINX-01

```
[root@nginx01 ~]# cat /etc/nginx/nginx.conf

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

stream{

    upstream loren {
        least_conn;
        server 10.0.0.33:80 weight=1;
        server 10.0.0.153:80 weight=1;
    }

    server {
         listen       8080;
         proxy_pass loren;
    }
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

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}


[root@nginx01 ~]# cat /etc/keepalived/keepalived.conf
! Configuration File for keepalived

global_defs {
    enable_script_security
    script_user root
}


vrrp_script check_nginx
{
    script "/sbin/pidof nginx"
    interval 2
    fall 2
    rise 2
}


#VRRP configuration for the VNIC in the transit subnet
vrrp_instance ISV {
    state MASTER
    interface ens3
    track_interface {
       ens3
    }
    virtual_router_id 51
    priority 200
    unicast_src_ip 10.0.0.149
    unicast_peer {
     10.0.0.229
    }
    authentication {
        auth_type PASS
        auth_pass ISV-test
    }

     track_script {
        check_nginx
    }

    notify_master /root/claim-vips-notify-master.sh
}



[root@nginx01 ~]# cat claim-vips-notify-master.sh
#!/bin/bash

/bin/oci network vnic assign-private-ip --vnic-id  ocid1.vnic.oc1.ap-tokyo-1.abxhiljr763m6cu575tf5vn72bokbcwss4f4y52eompbof25z4cq6lvoyd7q  --ip-address 10.0.0.100 --unassign-if-already-assigned

ip addr add 10.0.0.100/24 dev ens3 label ens3:0
```

NGINX-02

```
[root@nginx02 ~]# cat /etc/nginx/nginx.conf

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

stream{

    upstream loren {
        least_conn;
        server 10.0.0.33:80 weight=1;
        server 10.0.0.153:80 weight=1;
    }

    server {
         listen       8080;
         proxy_pass loren;
    }
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

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}


[root@nginx02 ~]# cat /etc/keepalived/keepalived.conf
! Configuration File for keepalived

global_defs {
    enable_script_security
    script_user root
}

vrrp_script check_nginx
{
    script "/sbin/pidof nginx"
    interval 2
    fall 2
    rise 2
}


#VRRP configuration for the VNIC in the transit subnet
vrrp_instance ISV {
    state BACKUP
    interface ens3
    track_interface {
       ens3
    }
    virtual_router_id 51
    priority 100
    unicast_src_ip 10.0.0.229
    unicast_peer {
     10.0.0.149
    }
   authentication {
        auth_type PASS
        auth_pass ISV-test
    }

     track_script {
        check_nginx
    }

    notify_master /root/claim-vips-notify-master.sh
}


[root@nginx02 ~]# cat claim-vips-notify-master.sh
#!/bin/bash

/bin/oci network vnic assign-private-ip --vnic-id ocid1.vnic.oc1.ap-tokyo-1.abxhiljrovq4hfl54vviiuhdrsfrhuqdmtpobfwkfnb2nvec52lzuoffjkqa  --ip-address 10.0.0.100 --unassign-if-already-assigned

ip addr add 10.0.0.100/24 dev ens3 label ens3:0
```

#### 4. 启动服务

```
[root@nginx0xxxxx ~]# systemctl stop firewalld;
[root@nginx0xxxxx ~]# systemctl disable firewalld;
[root@nginx0xxxxx ~]# seenforce 0;

[root@nginx0xxxxx ~]# chmod 777 claim-vips-notify-master.sh;
[root@nginx0xxxxx ~]# systemctl enable nginx --now;
[root@nginx0xxxxx ~]# systemctl enable keepalived --now;

```

给NGINX-01配置VIP

```
[root@nginx01 ~]# ./claim-vips-notify-master.sh

```

#### 5. 模拟故障

```
[root@nginx01 ~]# systemctl stop nginx;

```
