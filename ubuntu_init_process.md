
## Ubuntu开机启动程序配置


1. 创建systemd服务

```

root@demo:~# cat /lib/systemd/system/loren.service
#  SPDX-License-Identifier: LGPL-2.1+
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

# This unit gets pulled automatically into multi-user.target by
# systemd-rc-local-generator if /etc/rc.local is executable.

[Unit]
Description=loren test
ConditionFileIsExecutable=/etc/loren.local
After=network.target

[Service]
Type=forking
ExecStart=/etc/loren.local start
TimeoutSec=0
RemainAfterExit=yes
GuessMainPID=no

[Install]
WantedBy=multi-user.target

```

2. 配置启动执行脚本

```
root@demo:~# cat /etc/loren.local
#!/bin/sh

echo "loren test" >> /tmp/loren.txt


root@demo:~# chmod 755 /etc/loren.local

root@demo:~# ls -l /etc/loren.local
-rwxr-xr-x 1 root root 47 Oct  9 07:45 /etc/loren.local

```

3. 使能该服务

```
root@demo:~# systemctl daemon-reload
root@demo:~# systemctl enable loren.service
Created symlink /etc/systemd/system/multi-user.target.wants/loren.service → /lib/systemd/system/loren.service.

```

4. 重启虚拟机，验证效果

```
root@demo:~# cat /tmp/loren.txt
loren test
```
