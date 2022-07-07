

1. 创建CICD分区

![image](https://user-images.githubusercontent.com/4653664/177750139-a9787dbb-f6f7-4885-8a3d-ad4b40d0e471.png)

![image](https://user-images.githubusercontent.com/4653664/177750069-b9fc7464-c18d-445b-a17b-9a4570afd0b7.png)


2. 权限配置

创建动态组

![image](https://user-images.githubusercontent.com/4653664/177751359-136d4a16-0e16-49ee-b8a9-821108de2a7b.png)

![image](https://user-images.githubusercontent.com/4653664/177751553-e1c4af9a-eb77-4375-a858-25a4b071665c.png)

创建IAM策略允许分区中的动态组访问OCI资源

![image](https://user-images.githubusercontent.com/4653664/177752610-010ab952-c3bf-4354-80b0-1f6c1984cfe0.png)


```
Allow dynamic-group BuildDynamicGroup to manage repos in compartment cicd
Allow dynamic-group BuildDynamicGroup to read secret-family in compartment cicd
Allow dynamic-group BuildDynamicGroup to manage devops-family in compartment cicd
Allow dynamic-group BuildDynamicGroup to manage generic-artifacts in compartment cicd
Allow dynamic-group BuildDynamicGroup to use ons-topics in compartment cicd
```

![image](https://user-images.githubusercontent.com/4653664/177752643-8f2c0a94-1d40-40d1-9210-9b5ff8449d21.png)


3. 创建OKE

![image](https://user-images.githubusercontent.com/4653664/177766950-d0adb5c1-f14d-41a6-ada7-5fbed2fa8b18.png)

![image](https://user-images.githubusercontent.com/4653664/177767360-323748b8-6e01-4739-94ac-cd57912b57fc.png)

![image](https://user-images.githubusercontent.com/4653664/177767526-95d568ca-31b3-4021-80d1-dd3b04a28355.png)

![image](https://user-images.githubusercontent.com/4653664/177767655-ec6c35f5-bbc5-47b7-9ab5-b3b432dd52c8.png)

![image](https://user-images.githubusercontent.com/4653664/177767734-8669825e-21f5-4355-9cad-5f43b6b9aa2e.png)

> 由于OKE集群创建需要些时间，这里我们优先创建OKE集群资源

![image](https://user-images.githubusercontent.com/4653664/177769133-a4474188-cc60-4448-be0a-fa1887aa9991.png)

4. 创建代码仓库

![image](https://user-images.githubusercontent.com/4653664/177764397-d1fa3706-1b1f-4cd0-bc1b-e5f27468d604.png)

![image](https://user-images.githubusercontent.com/4653664/177764461-e2fbd102-c136-4098-b70e-2be2388ba9ce.png)

> 这里使用OCI DevOps自带的代码仓库，也支持对接gitlab、github等代码管理仓库

可以将下面代码仓库的代码上传到我们自建的以上代码仓库中

```
https://github.com/oracle-quickstart/oci-devops-node.git
```

上传完成后，即可在我们自建的代码仓库demo中看到相应的代码文件

![image](https://user-images.githubusercontent.com/4653664/177765147-1b0ecd80-604d-4e8c-873c-386ae3e1c483.png)

5. 创建制品仓库

由于我们构建的是容器镜像，所以这里我们创建个镜像仓库

![image](https://user-images.githubusercontent.com/4653664/177765458-31ed0717-8dcf-4f1d-8b94-4655b736a18d.png)

> 每个区域的镜像仓库的域名都不同，这里使用的是osaka region的服务。

![image](https://user-images.githubusercontent.com/4653664/177765586-d2fbd182-7160-4b38-83a7-c0073a2ea2d7.png)

6. 创建Build Pipeline

![image](https://user-images.githubusercontent.com/4653664/177765744-e87a2309-6374-41b7-83f5-60d594f1cfb2.png)

这里添加两个stage，注意stage的类型不同

![image](https://user-images.githubusercontent.com/4653664/177765994-879cdf74-105f-45e4-b788-b7c0d218530b.png)

两个stage的详细信息如下

![image](https://user-images.githubusercontent.com/4653664/177765837-e74e57e2-94df-46a4-9ee7-578554a81718.png)

![image](https://user-images.githubusercontent.com/4653664/177765914-96269599-3372-40fd-af9a-8763d3a7fdb7.png)

7. 执行Build Pipeline

![image](https://user-images.githubusercontent.com/4653664/177766193-fb2c8b38-ee19-4d1c-afc9-79c7f2f718d0.png)

![image](https://user-images.githubusercontent.com/4653664/177766264-d23cd405-4c55-4231-a892-9260aa80926c.png)

![image](https://user-images.githubusercontent.com/4653664/177767229-9a095e67-332f-4886-93e5-4f06edff61a6.png)


8. 查看Build Pipelines输出的制品

![image](https://user-images.githubusercontent.com/4653664/177768564-cf84e766-2c4b-40a9-9026-a0c4ed593770.png)

9. 创建环境

这里创建一个OKE的开发环境

![image](https://user-images.githubusercontent.com/4653664/177768805-ac7b2471-bf4d-4276-a071-2b8eca3b88a0.png)

![image](https://user-images.githubusercontent.com/4653664/177768859-89c24d19-2b44-41ea-b92d-2e4a9f9e36d8.png)

![image](https://user-images.githubusercontent.com/4653664/177768938-188c4b10-e92b-47c5-b46d-7acad2f3f05b.png)


20 准备kubernetes 

![image](https://user-images.githubusercontent.com/4653664/177772461-8544ba3d-6282-46f8-8f67-bdbc17e99fa8.png)

![image](https://user-images.githubusercontent.com/4653664/177773412-36aafbd6-8ade-4fae-9975-62540d8de1bc.png)

```
kind: Namespace
apiVersion: v1
metadata:
  name: ${namespace}
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-gettingstarted-deployment
  namespace: ${namespace}
spec:
  selector:
    matchLabels:
      app: node-gettingstarted
  replicas: 3
  template:
    metadata:
      labels:
        app: node-gettingstarted
    spec:
      containers:
        - name: node-gettingstarted
          # enter the path to your image, be sure to include the correct region prefix
          image: kix.ocir.io/axg4iwqwngsd/demo:${BUILDRUN_HASH}
          imagePullPolicy: Always
          ports:
            - containerPort: 3000
              protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: node-gettingstarted-service
  namespace: ${namespace}
  annotations: 
    service.beta.kubernetes.io/oci-load-balancer-shape: "10Mbps"
spec:
  type: LoadBalancer
  ports:
    - port: 80
      protocol: TCP
      targetPort: 3000
  selector:
    app: node-gettingstarted

```

![image](https://user-images.githubusercontent.com/4653664/177774238-6fb49450-93d0-4a67-af87-b174f7898b71.png)


![image](https://user-images.githubusercontent.com/4653664/177774347-851108ee-6128-45d6-b956-50bec4fabba4.png)

![image](https://user-images.githubusercontent.com/4653664/177774541-311c5453-dbea-438f-9195-978eead850e8.png)



20. 创建Deployment pipeline





![image](https://user-images.githubusercontent.com/4653664/177769310-354cfcca-6421-4789-a2a6-88a6f4104ddf.png)

![image](https://user-images.githubusercontent.com/4653664/177769382-42938545-ad56-4728-8dfe-13690f404831.png)

添加一个stage

![image](https://user-images.githubusercontent.com/4653664/177769462-cbcb2927-7d52-42f4-993c-5656c5d3f78b.png)

![image](https://user-images.githubusercontent.com/4653664/177774653-c5530da3-945b-4826-ac4d-02df3e5ece27.png)

![image](https://user-images.githubusercontent.com/4653664/177774723-b697917a-2e20-4a3f-9409-4da9fc454e39.png)

![image](https://user-images.githubusercontent.com/4653664/177774839-42a42615-3fe2-4358-a51e-abf1084e89ec.png)


![image](https://user-images.githubusercontent.com/4653664/177774985-52f82780-7781-46e0-86c6-4c29899b6ad4.png)

![image](https://user-images.githubusercontent.com/4653664/177775040-60f7f404-29ba-44cd-923d-782dfbd55c20.png)

![image](https://user-images.githubusercontent.com/4653664/177775813-92e9e17f-5f94-45e4-a492-f1714f9e96af.png)


