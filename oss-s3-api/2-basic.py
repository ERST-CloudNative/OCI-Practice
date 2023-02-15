# This is a sample Python script.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id="[xxx]",
    aws_secret_access_key="[xxxx]",
    region_name="ap-tokyo-1",  # Region name here that matches the endpoint
    endpoint_url="https://nrtgmiqqwji0.compat.objectstorage.ap-tokyo-1.oraclecloud.com"
    # Include your namespace in the URL
)

# 创建Bucket
s3.meta.client.create_bucket(Bucket='my-bucket')

# 上传小文件
s3.meta.client.upload_file('test.txt', 'my-bucket', 'hello.txt')

# # 下载文件
s3.meta.client.download_file('my-bucket', 'hello.txt', 'download_file.txt')

# 删除文件
s3.meta.client.delete_object(Bucket='my-bucket', Key='hello.txt')

# 删除Bucket
s3.meta.client.delete_bucket(Bucket='my-bucket')

res = s3.meta.client.list_buckets()

# xx = json.dumps(res, indent=4, default=str)
# print(xx)

# 查看Bucket列表
for i in res['Buckets']:
    print(i['Name'])


