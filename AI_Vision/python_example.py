# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import base64
import json
import oci
import uuid

# https://docs.oracle.com/en-us/iaas/api/#/en/vision/20220125/AnalyzeImageResult/AnalyzeImage
# https://github.com/oracle-japan/ai-services-tutorials/tree/main/vision
# https://docs.oracle.com/en-us/iaas/vision/vision/using/pretrained_image_analysis_models.htm#pretrained_image_analysis_object_detect
# https://github.com/oracle-samples/oci-data-science-ai-samples

for i in range(1, 2):
    # 图片路径
    input_path = "C://Users//loren//PycharmProjects//visiondemo//test.jpg"
    # 单一图片中最多识别多少个目标对象
    # max_results = 5

    config = oci.config.from_file("C://Users//loren//PycharmProjects//visiondemo//config")

    # 读取图片数据
    with open(input_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    # 获取客户端
    ai_service_vision_client = oci.ai_vision.AIServiceVisionClient(config=config)

    # # image details-图片数据
    # inline_image_details = oci.ai_vision.models.InlineImageDetails()
    # inline_image_details.data = encoded_string.decode('utf-8')
    #
    # # features-使用的模型
    # image_object_detection_feature = oci.ai_vision.models.ImageObjectDetectionFeature()
    # image_object_detection_feature.max_results = max_results
    # features = [image_object_detection_feature]
    #
    # # 待分析请求的详细信息：图片数据和模型
    # analyze_image_details = oci.ai_vision.models.AnalyzeImageDetails()
    # analyze_image_details.image = inline_image_details
    # analyze_image_details.features = features
    #
    # # 发起图片目标识别请求
    # res = ai_service_vision_client.analyze_image(analyze_image_details=analyze_image_details)
    #
    # # 输出结果，其中包括识别目标对象的坐标
    # res_json = json.loads(repr(res.data))
    # print(json.dumps(res_json, indent=4))

    # 发起图片目标识别请求
    analyze_image_response = ai_service_vision_client.analyze_image(
        analyze_image_details=oci.ai_vision.models.AnalyzeImageDetails(
            features=[
                oci.ai_vision.models.ImageObjectDetectionFeature(
                    feature_type="OBJECT_DETECTION",
                    max_results=5,
                    model_id=oci.ai_vision.models.ImageObjectDetectionFeature().model_id)],
            image=oci.ai_vision.models.InlineImageDetails(
                source="INLINE",
                data=encoded_string.decode('utf-8')),
            compartment_id="ocid1.compartment.oc1..aaaaaaaaio757zvh35zqqg7xfh6yusmwylr3qdm2lpth3e2vyfsg47f3mv7q"),
        opc_request_id=uuid.uuid4().__str__())

    # Get the data from response
    print(analyze_image_response.data)

# 示例：
# {
#   "errors": [],
#   "image_classification_model_version": null,
#   "image_objects": [
#     {
#       "bounding_polygon": {
#         "normalized_vertices": [
#           {
#             "x": 0.04220779220779221,
#             "y": 0.1951219512195122
#           },
#           {
#             "x": 0.3474025974025974,
#             "y": 0.1951219512195122
#           },
#           {
#             "x": 0.3474025974025974,
#             "y": 0.725609756097561
#           },
#           {
#             "x": 0.04220779220779221,
#             "y": 0.725609756097561
#           }
#         ]
#       },
#       "confidence": 0.9778019,
#       "name": "Person"
#     },
#     {
#       "bounding_polygon": {
#         "normalized_vertices": [
#           {
#             "x": 0.35714285714285715,
#             "y": 0.4695121951219512
#           },
#           {
#             "x": 0.4902597402597403,
#             "y": 0.4695121951219512
#           },
#           {
#             "x": 0.4902597402597403,
#             "y": 0.7804878048780488
#           },
#           {
#             "x": 0.35714285714285715,
#             "y": 0.7804878048780488
#           }
#         ]
#       },
#       "confidence": 0.7862462,
#       "name": "Box"
#     }
#   ],
#   "image_text": null,
#   "labels": null,
#   "object_detection_model_version": "1.3.85",
#   "ontology_classes": [
#     {
#       "name": "Box",
#       "parent_names": [
#         "Office supplies"
#       ],
#       "synonym_names": []
#     },
#     {
#       "name": "Person",
#       "parent_names": [],
#       "synonym_names": []
#     },
#     {
#       "name": "Office supplies",
#       "parent_names": [],
#       "synonym_names": []
#     }
#   ],
#   "text_detection_model_version": null
# }
