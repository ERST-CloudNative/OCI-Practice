
# 添加API KEY

![image](https://user-images.githubusercontent.com/4653664/221759161-d8c6a441-03ac-4829-b1b6-2395e0f4a404.png)


### 创建policy

```
Allow group queue-user to manage queues in tenancy
Allow group queue-user to use queue-push in tenancy
Allow group queue-user to use queue-pull in tenancy
Allow group queue-user to read queues in tenancy
```

### 示例代码(OCI-SDK-Python)

```
# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import uuid

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file(file_location="C://Users//loren//PycharmProjects//queue//config")

# Initialize service client with default config file
queue_client = oci.queue.QueueClient(config)

opc_request_id = str(uuid.uuid4())

# Send the request to service, some parameters are not required, see API
# doc for more info
queue_client.base_client.endpoint = "https://cell-1.queue.messaging.eu-frankfurt-1.oci.oraclecloud.com"
put_messages_response = queue_client.put_messages(
    queue_id="ocid1.queue.oc1.eu-frankfurt-1.amaaaaaanthnqxqa4m4tp2ujng4rpoz223alyvqgwg6ggonrwodmce5gkvca",
    put_messages_details=oci.queue.models.PutMessagesDetails(
        messages=[
            oci.queue.models.PutMessagesDetailsEntry(
                content="Hello Queue")]),
    opc_request_id=opc_request_id)
#
# # Get the data from response
print(put_messages_response.data)

```
