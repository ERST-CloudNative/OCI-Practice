
1. 使能区间`Amazon S3 API`兼容性

![image](https://user-images.githubusercontent.com/4653664/216957199-1697a4a2-88b8-459f-9dd9-c6126380da8e.png)

2. 获取`aws_access_key_id`、`aws_secret_access_key`

首先通过生成`Serect Key`获取`aws_secret_access_key`

![image](https://user-images.githubusercontent.com/4653664/216957494-557cb978-3cfc-4eac-8c6c-1e8e5e465b91.png)

产生`Secret Key`之后就可以查看到`aws_access_key_id`

![image](https://user-images.githubusercontent.com/4653664/216959549-266823a1-9917-41fd-b9f3-eefd09dbaf41.png)

3. 获取region_name

![image](https://user-images.githubusercontent.com/4653664/216957891-827cfc52-c86b-4706-8ee3-e2d83f75426b.png)


4. 获取endpoint_url

endpoint列表：https://docs.oracle.com/en-us/iaas/api/#/en/s3objectstorage/20160918/

其中的namespace可以通过下图获取

![image](https://user-images.githubusercontent.com/4653664/216960288-d3265e06-39b0-4e4e-b77d-6869dae31362.png)

5. 测试代码

```
# This is a sample Python script.
import boto3

# dRdEkuKk5lShQNFtnlIPtidXRQTR5TQKJLY9JWO6/xY=

s3 = boto3.resource(
    's3',
    aws_access_key_id="[xxx]",
    aws_secret_access_key="[xxx]",
    region_name="ap-tokyo-1",  # Region name here that matches the endpoint
    endpoint_url="https://nrtgmiqqwji0.compat.objectstorage.ap-tokyo-1.oraclecloud.com"
    # Include your namespace in the URL
)

# Print out the bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
```




