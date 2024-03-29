## VM串口使用示例


### 1. 权限配置


创建用户组，并将相关用户添加到用户组

<img width="824" alt="1689838026942" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1d71ab85-4773-4c35-b46c-a164af2571bd">


创建策略

<img width="825" alt="1689839447448" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e0381d82-b81e-492d-b995-33461b36fca6">


```
Allow group vm-console-group to manage instance-console-connection in tenancy
Allow group vm-console-group to read instance in tenancy
```


### 2. 实践案例-忘记密码

> 注意，这个场景仅适用于忘记root用户密码，如果是普通用户密码，请联系Linux管理员进行重置密码。

默认情况,Oralce Linux8 禁用了密码登录认证方式，这里为了实验效果，需要开启sshd的密码认证配置

```
[root@demo ~]# vi /etc/ssh/sshd_config

# To disable tunneled clear text passwords, change to no here!
PasswordAuthentication yes
#PermitEmptyPasswords no
#PasswordAuthentication no

[root@demo ~]# systemctl restart sshd
```

启动Cloud Shell连接

<img width="838" alt="1689841565180" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3d70b62d-248e-4d78-8793-2ec800e140ce">

重启虚拟机

<img width="702" alt="1689841494806" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/eb8c70a1-a920-4824-86b0-06ef3ef9d2ec">

启动过程中，可以多次按"ESC"键进入GRUB界面

<img width="672" alt="1689841758261" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ac2d45dd-d41b-40b9-820b-f42c569e1552">

然后按"e"键进入编辑模式

<img width="681" alt="1689841980715" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5b102e4e-5552-4282-9d2a-3ac09d51faa4">

进入编辑模式后，在'Linux'那行行末添加以下配置，这条配置将中断启动流程，并禁止SELinux

<img width="631" alt="1689842854402" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c8133583-b96e-451d-a46f-9d449b4a7d73">

```
rd.break enforcing=0
```

然后，按"ctrl-x"以编辑过的参数配置启动

<img width="583" alt="1689844479616" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e2532414-c35a-4de3-88a4-66024e32e754">

默认`/sysroot/`下的挂载的文件系统是只读的，这里重新挂载文件系统，并配置读写权限,然后切换到`/sysroot`下，修改密码,SELinux重新打标签

<img width="435" alt="1689844713151" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/274c8d03-f705-4012-8af1-e4ae577d7b6f">

```
sh-4.4# mount -o remount,rw /sysroot
sh-4.4# chroot /sysroot
sh-4.4# passwd YOUR_USERS_XXXX
sh-4.4# touch /.autorelabel
# 退出并重启
sh-4.4# exit
switch_root:/# reboot -f
```

验证使用可以通过新的密码进行登录

<img width="652" alt="1689850368968" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/31119f70-0faf-40b9-a2c2-e50a83520388">









