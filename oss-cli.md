

##### 创建Bucket

```
oci os bucket create --name ociaabucket-ocioci  --compartment-id ocid1.compartment.oc1.xxxxx
```

##### 查看Bucket

```
oci os bucket list  --compartment-id ocid1.compartment.oc1..aaa.xxx
```

##### multi-part 上传

```
dd if=/dev/zero of=./test.bin bs=4M count=128

oci os object put --bucket-name ociaabucket-console --file test.bin --name test.bin --part-size 4 --parallel-upload-count 10
Upload ID: 58dfdd66-9979-3368-0837-d7d9a40e4760
```

##### 配置policy（lifecycyle）

```
allow service objectstorage-ap-tokyo-1 to manage object-family in compartment osstest
```

```
allow group storageadmins to manage vaults in compartment osstest
allow group storageadmins to manage keys in compartment osstest
allow service objectstorage-ap-tokyo-1 to use keys in compartment osstest
```

##### Pre-Authenticated Requests

```
curl https://objectstorage.ap-tokyo-1.oraclecloud.com/p/cddddddddddddddddddd/n/nrtgmiqqwji0/b/s3/o/ --upload-file 1.txt

```
