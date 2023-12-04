

## OKE网络规划与集群创建

### 1. 网络规划

```
public subnet(Node Pool/API): 10.0.0.0/18(可容纳16000+容器)
Service LB subnet： 10.0.64.0/18
private subnet:	10.0.128.0/18
bussiness unit 01: 10.0.0.192/24(可选)
bussiness unit 02: 10.0.0.193/24（可选）
```
### 2. VCN配置

创建VCN

<img width="481" alt="1701693246888" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/7ce8855a-a7ab-4e80-9adb-cb3e5ec6252a">

<img width="657" alt="1701693370452" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ffbbff70-60c9-48d6-b76e-8955c24485aa">

<img width="719" alt="1701693410269" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/dec047fe-593d-4cff-bf29-29e1b432ddee">

创建所需的子网(Service LB subnet)

<img width="901" alt="1701693610019" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f3a571fc-f4fa-428f-a015-be9c5a8d67bf">

其中，Security Lists可以新建或者使用默认的配置，这里选择默认配置

<img width="620" alt="1701693665280" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d435ec78-6d56-40ee-ab4a-504ba2c28d48">

配置默认的安全列表，这里添加两天安全规则：
1. 允许节点间通信
2. 允许访问master集群api端口

<img width="944" alt="1701693753666" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/03b32034-b179-4171-af24-0d8b51a561a6">

### 3. OKE集群创建

<img width="481" alt="1701693841224" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1e4a9e04-0339-46fe-8286-4c4438f1df77">

<img width="753" alt="1701693880663" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/86c27df3-5a4f-49be-a8eb-ed4ca4f1d089">

<img width="794" alt="1701693931930" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/f40a2c8b-184e-498b-9c9e-55015870abb9">

<img width="900" alt="1701693973180" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ea0e86d5-d907-4fde-b288-7d4c341661a8">

<img width="930" alt="1701694022603" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/fffdd8d5-393b-4fb6-b470-3ce90211f0e4">

<img width="823" alt="1701694278107" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/437720f5-bff2-4547-875a-d28c3697179f">

<img width="958" alt="1701694331319" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/87c5e5b5-152d-45d0-9c15-05e02b4052fe">

<img width="867" alt="1701694362814" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c29abd75-2bb1-482e-aaec-25a745306295">

<img width="960" alt="1701694399763" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/df7401e9-ff82-4a70-a6c8-293e0a98e16c">




