## OCI堡垒机


### 1. 环境配置

#### IAM权限配置

创建两个用户组`SecurityAdmins`和`BastionUsers`,并将相关用户加入到用户组中

<img width="858" alt="1685095850473" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5e9dbf17-89fe-45b1-800e-43d69470e52b">

<img width="758" alt="1685095937622" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/27ab3473-699a-47fa-9e8d-c57e0be56c16">


创建policy

```
Allow group BastionUsers to use bastions in tenancy
Allow group BastionUsers to read instances in tenancy
Allow group BastionUsers to read vcn in tenancy
Allow group BastionUsers to manage bastion-session in tenancy
Allow group BastionUsers to read subnets in tenancy
Allow group BastionUsers to read instance-agent-plugins in tenancy
Allow group BastionUsers to read vnic-attachments in tenancy
Allow group BastionUsers to read vnics in tenancy

Allow group SecurityAdmins to manage bastion-family in tenancy
Allow group SecurityAdmins to manage virtual-network-family in tenancy
Allow group SecurityAdmins to read instance-family in tenancy
Allow group SecurityAdmins to read instance-agent-plugins in tenancy
Allow group SecurityAdmins to inspect work-requests in tenancy
```

<img width="716" alt="1685096102095" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b06f3822-8749-41a8-8082-3e9c88173f35">

#### 笔记本配置

默认WIN10上禁用了RSA签名，这里需要添加`config`配置文件内容以启用RSA签名.

> MAC/Linux可以参考配置

```
loren@loren-1TKWTQ3 MINGW64 ~/Desktop $ cat  ~/.ssh/config

Host *
    HostkeyAlgorithms +ssh-rsa
    PubkeyAcceptedAlgorithms +ssh-rsa
```


### 2. 创建堡垒机

<img width="823" alt="1685096196167" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c91d7443-b025-4790-87a3-5331b1167eb1">

### 3. 通过SSH到内网VM(Managed SSH)

首先，需要在对应的虚拟机上开启`bastion`插件

<img width="795" alt="1685096302575" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/55175822-ef3d-4806-b0d6-9b5c7d1da819">

创建`session`

<img width="857" alt="1685096755576" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/7da85081-2646-4460-b2d0-d04cf34fed00">

拷贝连接命令行

<img width="798" alt="1685096816788" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/a2dfbe0e-d94c-4543-a499-b20cceb974f2">

> 记得替换使用自己下载的私钥

连接验证

```
$ ssh -i ssh.key -o ProxyCommand="ssh -i ssh.key -W %h:%p -p 22 ocid1.bastionsession.oc1.ap-tokyo-1.asmasassdsx7x5pnzfha@host.bastion.ap-tokyo-1.oci.oraclecloud.com" -p 22 opc@10.0.30.10

The authenticity of host '10.0.30.10 (<no hostip for proxy command>)' can't be established.
ED25519 key fingerprint is SHA256:KhOnGqcXRA5bXi2erTAJTyKUqhBIALvHzFdm+IvWLuI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.0.30.10' (ED25519) to the list of known hosts.
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Fri May 26 09:30:52 2023 from 138.2.28.189
[opc@opensearch-test ~]$

```

### 4. 通过SSH端口转发访问内网web应用(Port forwarding)

这里以`OpenSearch Dashboard`为例，创建`session`

<img width="954" alt="1685097031866" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8541e20f-54df-4d77-b810-b8b1ed144415">

按照上小节同样的方式拷贝SSH命令行

```
 ssh -i 5601.key -N -L 5601:10.0.30.68:5601 -p 22 ocid1.bastionsession.oc1.ap-tokyo-1.amaaaaaamxdwssd5xq6fhsdsf6ksdsvfqjlq@host.bastion.ap-tokyo-1.oci.oraclecloud.com
```

本地访问

<img width="955" alt="1685097203820" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/23dd7533-0c6b-48b7-af2a-4b3268f6fa6b">




