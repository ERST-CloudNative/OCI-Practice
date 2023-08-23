## 自定义镜像操作


### 1. 跨区间使用镜像

示例： 在区间demo下创建虚拟机时，使用test区间下的自定义镜像

<img width="958" alt="1692756362085" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/a4992b1b-ce0b-4120-8ac2-5a972ba4cd32">


### 2. 跨region使用镜像

#### Region-A操作(South Korea North (Chuncheon))

首先，创建对象存储bucket，用于存储导出的镜像

<img width="959" alt="1692756507909" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e30c6ffc-9923-4a23-b7ac-f693c9492db2">


将镜像导出到对象存储中

<img width="949" alt="1692756636203" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1be43916-d5c3-4796-bc5a-64a185c9696a">

<img width="634" alt="1692757293497" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/c0a80517-183f-4d47-a3a1-c0b877dc25f7">

镜像正在导出中

<img width="941" alt="1692757357233" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/6f5b7892-92b7-4a57-af1a-c6e5312dbdc5">

导出完成

<img width="959" alt="1692757940139" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/98d31304-a099-4739-a03f-6e6242459ad7">

针对镜像文件，在对象存储中，创建Pre-Authenticated Requests(预认证请求)

<img width="953" alt="1692758541732" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5bb82f74-34af-4920-a280-d5db61ad6f6f">

<img width="631" alt="1692758629213" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/0715d2b6-1854-4c0f-83ec-e3cb740f0a4e">

<img width="480" alt="1692758696530" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/508b4605-eed1-43bc-b8a5-f7615337656f">


保存预认证请求的URL信息，后续从其它区域导入镜像时使用，URL类似如下的格式

```
https://objectstorage.ap-chuncheon-1.oraclecloud.com/p/doW_6NO6pkto5uDg1RIGo5cMIhO7ojORA-4m-e3ujFG8JYMLgE-b6b4Z8twvYTIx/n/axiafq1kyzu0/b/imagetest/o/exported-image-20230823-1010
```

#### Region-B操作(Singapore (Singapore))

切换region,导入镜像

<img width="956" alt="1692758758161" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ca713299-63a1-45cb-b7ba-37f11330252d">


其中，Object Storage URL为Region-A中创建的Pre-Authenticated Requests(预认证请求)的URL。

<img width="954" alt="1692759430738" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/d3138498-932e-4656-a454-bbd9cb5d0a0a">


待镜像导入完成后，即可以正常使用镜像创建虚拟机了。

<img width="957" alt="1692759495608" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/0307ac09-3e9f-47dd-adc2-5b306a7c2af3">


