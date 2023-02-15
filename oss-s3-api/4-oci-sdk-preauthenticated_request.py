# https://github.com/oracle/oci-python-sdk/tree/master/examples

import oci
import datetime
import requests
import pytz
from oci.config import from_file
from oci.object_storage.models.create_preauthenticated_request_details import *

config = from_file(file_location="config")

object_storage = oci.object_storage.ObjectStorageClient(config)

compartment_id = config["tenancy"]
namespace = object_storage.get_namespace().data
bucket_name = "test"
object_name = "cat.webp"
# my_data = b"Hello, World!"
par_name = "test"

par_ttl = (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).replace(tzinfo=pytz.UTC)

create_par_details = CreatePreauthenticatedRequestDetails()
create_par_details.name = par_name
create_par_details.object_name = object_name
create_par_details.access_type = CreatePreauthenticatedRequestDetails.ACCESS_TYPE_OBJECT_READ
create_par_details.time_expires = par_ttl.isoformat()

par = object_storage.create_preauthenticated_request(namespace_name=namespace, bucket_name=bucket_name,
                                                     create_preauthenticated_request_details=create_par_details)

# Get Object using the Pre-Authenticated Request
par_request_url = object_storage.base_client.get_endpoint() + par.data.access_uri

# download cat.webp image
r = requests.get(par_request_url)
with open('cat.webp', 'wb') as code:
    code.write(r.content)

# Delete Pre-Authenticated Request
object_storage.delete_preauthenticated_request(namespace_name=namespace, bucket_name=bucket_name, par_id=par.data.id)

# print("Deleting object {}".format(object_name))
# object_storage.delete_object(namespace, bucket_name, object_name)

# print("Deleting bucket {}".format(bucket_name))
# object_storage.delete_bucket(namespace, bucket_name)
