## OCI 云卫士实践

对云资源的需求正在以令人难以置信的速度增长。要检查和保护的原始资源数量极大地压垮了大多数信息安全团队的现有流程和工具。

云服务增长持续扩大，客户需要供应商提供更多帮助来应用真正的安全性。仅 Oracle 就提供了超过 60 个云应用程序和服务，这可能给客户带来巨大的挑战。

信息安全需求不断增长。威胁正在扩大。更多的服务意味着需要更多的知识来保护它们。技能和人力方面的差距继续扩大，超出了现有的专业知识。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/93eedfc9-d7e9-4424-a117-7e426d1b1bcb)


Oracle Cloud Guard 是一个统一的安全解决方案，提供全球集中的方法来保护所有客户的资产。它可以自动分析数据、检测威胁和错误配置，然后追捕并消除这些安全威胁，而无需人工监督。
Oracle Cloud Guard 持续从基础设施和应用程序堆栈的各个部分收集数据，包括审核日志、Oracle Data Safe、Oracle OS Management Service 以及第三方产品。
Oracle Cloud Guard 主动检测并停止其识别的异常活动，自动关闭恶意实例，并在检测到异常用户行为时主动撤销用户权限。


### 第 1 步：环境准备

1. 从左侧导航面板中选择“Identity & Security” ，然后单击“Cloud Guard”。

<img width="403" alt="1708585414557" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/2d34f028-b37d-4f23-8710-fc5494e39af3">


2. 启用云卫士

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/a963cd03-09a5-4017-82b5-45731675ba85)

<img width="953" alt="1708585541955" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/a2df7fab-a365-4d7c-b9c8-936f71b96afe">

<img width="666" alt="1708585632239" src="https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/56e7155e-4a9d-4280-9f0b-5aae8501ae0d">



### 第 2 步：注册新目标

1. 从左侧导航面板中选择“目标” ，然后单击“创建目标”。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/814a1d00-12e5-4183-bdeb-959bc4b6cb86)


2. 提供以下信息:

- 目标名称：目标+ （您名字的首字母和姓氏）
- 描述：目标+ （您名字和姓氏的首字母）
- 在“学习者” 下选择分配给您的隔间（您姓名的首字母和姓氏）
- 选择默认配置检测器配方
- 选择默认的活动检测器配方
- 选择默认响应程序配方
- 单击创建
> 注意：威胁检测器配方已应用于根分区级别，以捕获跨分区的用户活动（必需）。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/fa4bbdd6-988d-4107-b67f-e06ecfd12fd5)


3. 创建目标后，您将被重定向到您的目标信息。您可以探索 Cloud Guard 的检测器和响应器配方提供商，以识别偏差并主动修复这些问题。完成后，单击屏幕左上角的Cloud Guard超链接返回主仪表板。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b6d9a20d-17c2-43d1-8039-728524ab22ae)


### 第 3 步：创建认可资源

1. 打开位于屏幕左侧的常规菜单，单击“存储”并选择“对象存储和归档”,单击创建存储桶。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3b2eb0fd-eea1-4af0-9a6f-5acde7842ebf)


2. 输入存储桶名称并单击创建。出于跟踪目的，我们建议使用以下名称约定：

bucket-CoSE-您的缩写

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3a3b97bf-67c5-4975-ae25-63ebc3591753)


3. 返回存储桶列表，单击最近创建的存储桶

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b289120d-bca6-4b71-9fec-cdd9e193a5fe)


4. 查看信息，然后单击“编辑可见性”

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/3b10b98f-3055-473e-bd5a-661522166189)


5. 将可见性更改为PUBLIC，然后单击“保存更改”

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ce91cbf7-d18c-4cc5-8ccd-9a3a493167e4)


6. 现在这个桶已经被公开曝光了。不用担心，我们将在接下来的几分钟内修复此问题。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/eddc70a7-a792-47ba-8bb1-cf83b807faa0)


7. 此外，继续使用默认名称和设置为其创建 5 到 10 个预验证请求。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/37f755ac-9aea-4936-8267-ee44eea3aafd)


### 第 4 步：执行补救措施

1. 打开位于屏幕左侧的常规菜单，单击“安全”并选择“Cloud Guard”。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/1d3d2e93-7d66-4ed1-a76a-df77c77a622e)


2. 在主仪表板中，您将看到您的环境状态和当前要修复的活动。考虑到我们最近创建了一个存储桶，在控制台中查看更新可能需要长达 15 分钟的时间。

3. 几分钟后，您将看到报告的新警报。如您所见，我们可以识别存储桶中的设置引发的问题。您可以单击屏幕左侧的问题来进一步调查问题。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/87613a83-bc75-455d-9fa0-75e4ef8fbb38)


> 注意：警报可能最多需要 20 分钟才会显示在仪表板中

4. 如您所见，我们的 Bucket 公共警报在 Oracle Managed Detector 列表中默认配置为“严重” 。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/9354144c-653b-4f8b-b0c8-bb8bf6588de4)


5. 让我们深入探讨一下这个问题。单击屏幕左侧的“响应者活动” 。我们可以轻松识别问题、资源以及执行状态和类型。单击问题名称Bucket is Public链接。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/26bd3ed1-5a2f-4a07-a2c4-b76f3ea22bbe)


6. 在此页面上，我们可以看到有关问题、风险级别、状态、资源和建议的详细信息。作为安全分析师，如果您已手动修复此任务，则可以将此问题标记为已解决；如果您认为这是错误的，则可以忽略它。然而; 我们知道这是一个严重的暴露，所以让我们修复它。单击修复这将触发操作并将存储桶恢复为私有。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/ed017cb0-b8c5-4558-a918-dd87ab52ffa4)


7. 检查操作并单击修复

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/5a555113-c5cf-4ae1-bed9-e5dd23f96574)


8. 单击“添加语句”将策略添加到您的分区中。这将允许 Cloud Guard 继续执行修复过程。单击修复。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/b27895ac-c569-4103-b276-5be50bc35980)


9. 最后，返回Cloud Guard仪表板，您将看到该操作现已修复。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/8f32a809-6842-4b4e-92b5-ad7312a71c5a)


### 第 5 步：验证补救措施

打开位于屏幕左侧的常规菜单，单击“存储”，然后选择“对象存储和归档”

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/fe16b237-be4a-429d-94b3-24994d228ac5)

选择分配给您的车厢。您可以在Oracle Cloud选项卡中的Luna Lab网页中找到它。打开您创建的存储桶，您现在将看到它是私有的。

![image](https://github.com/ERST-CloudNative/OCI-Practice/assets/4653664/e04359dc-0dce-4c10-8e66-740e282ad191)

