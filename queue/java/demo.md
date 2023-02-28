
示例代码

```
package org.example;

import com.oracle.bmc.ConfigFileReader;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.queue.QueueClient;
import com.oracle.bmc.queue.model.PutMessagesDetails;
import com.oracle.bmc.queue.model.PutMessagesDetailsEntry;
import com.oracle.bmc.queue.requests.PutMessagesRequest;
import com.oracle.bmc.queue.responses.PutMessagesResponse;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello world!");

        final ConfigFileReader.ConfigFile configFile = ConfigFileReader.parse("C:\\Users\\loren\\IdeaProjects\\queue\\src\\main\\resources\\config");
        final AuthenticationDetailsProvider provider = new ConfigFileAuthenticationDetailsProvider(configFile);

        /* Create a service client */
        QueueClient client = new QueueClient(provider);
        client.setEndpoint("https://cell-1.queue.messaging.eu-frankfurt-1.oci.oraclecloud.com");

        /* Create a request and dependent object(s). */
        PutMessagesDetails putMessagesDetails = PutMessagesDetails.builder()
                .messages(new ArrayList<>(Arrays.asList(PutMessagesDetailsEntry.builder()
                        .content("Hello FeiYou 2023").build()))).build();

        PutMessagesRequest putMessagesRequest = PutMessagesRequest.builder()
                .queueId("ocid1.queue.oc1.eu-frankfurt-1.amaaaaaanthnqxqa4m4tp2ujng4rpoz223alyvqgwg6ggonrwodmce5gkvca")
                .putMessagesDetails(putMessagesDetails)
                .opcRequestId("0M20ZFHD84BUPN2UD4JD").build();

        /* Send request to the Client */
        PutMessagesResponse response = client.putMessages(putMessagesRequest);

        System.out.println(response.toString());
    }
}
```

配置文件信息

```
[DEFAULT]
user=ocid1.user.oc1..aaaaaaaakww2ubgm2m7sui55tosprd66wsn7slmqjzt2rnyydhnbx2dzxmcq
fingerprint=1f:c2:28:a0:64:59:d6:64:15:c2:f9:1f:34:ae:a9:bb
tenancy=ocid1.tenancy.oc1..aaaaaaaaxtx2fueldyrzmlfaa3pnvxylcx2hmtacpk3pmy42rzpjq4yizysq
region=eu-frankfurt-1
key_file=C:\Users\loren\IdeaProjects\queue\src\main\resources\test.pem
```

测试效果

![image](https://user-images.githubusercontent.com/4653664/221863543-919436e4-8736-40ac-90bb-71a1a07f3e3d.png)

![image](https://user-images.githubusercontent.com/4653664/221863742-60eaeff9-3063-4619-be73-a222f6426f18.png)




