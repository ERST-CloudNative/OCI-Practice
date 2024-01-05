
### redis-cli安装

OS: ubuntu 18

```
apt-get update
apt install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
apt-get install redis-tools
redis-cli --version
```

OS: Oracle Linux 8

```
wget https://download.redis.io/releases/redis-7.0.5.tar.gz
tar zxvf redis-7.0.5.tar.gz
cd redis-7.0.5/
yum install -y openssl
make BUILD_TLS=yes;make install
cd src;cp redis-server /usr/bin/;cp redis-cli /usr/bin/;cp redis-trib.rb /usr/bin/
```

验证方式

```
redis-cli --tls -h amsssssssssssssstce7pa-p.redis.ap-chuncheon-1.oci.oraclecloud.com -p 6379
```
