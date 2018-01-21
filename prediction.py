import httplib, urllib, base64
import json
from pprint import pprint
import webbrowser


#################### PREDICTION ####################

pre_headers = {
        # Request headers
        'Prediction-key': '267a64e2d25e43859e0d2fb308c43813',
        }

pre_params = urllib.urlencode({
        # Request parameters
        'iterationId': '76d87955-70d0-48d9-9007-5de607882b53',
        'projectId': 'be7c629e-3887-4622-92b9-02df9f0315c6'
        })
with open("exp_date_example2.jpg", "rb") as imageFile:
  f = imageFile.read()
  body = bytearray(f)

#body = "{'url':'https://i2.wp.com/www.peanutbutterlist.com/wp-content/uploads/2015/02/groceries.jpg?fit=1000%2C508'}"

try:
    conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v1.1/Prediction/be7c629e-3887-4622-92b9-02df9f0315c6/image?%s" % pre_params, body, pre_headers)
    response = conn.getresponse()
    pre_data = response.read()
    print("PRE-DATA")
    print(pre_data)
    conn.close()

except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

###################### OCR ##############################
# Replace the subscription_key string value with your valid subscription key.
subscription_key = '4ef11bd7e4ec4e69bd1c1844160838ae'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

ocr_headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

ocr_params = urllib.urlencode({
    # Request parameters. The language setting "unk" means automatically detect the language.
    'language': 'en',
    'detectOrientation ': 'true',
})

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)
    conn.request("POST", "/vision/v1.0/ocr?%s" % ocr_params, body, ocr_headers)
    ocr_response = conn.getresponse()
    ocr_data = ocr_response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    print("OCR-DATA")
    print(ocr_data)
    conn.close()

except Exception as e:
    print('Error:')
    print(e)

ocr_json_data = json.loads(ocr_data)
obj_text = ocr_json_data["regions"]
# for word in obj_text:
#     word_text = word[]

pre_json_data = json.loads(pre_data)
obj_prediction = pre_json_data["Predictions"][0]["Tag"]
obj_id = pre_json_data["Id"]
obj_date = pre_json_data["Created"]

app_data = {}
app_data['obj_exp'] = 0
app_data['obj_prediction'] = obj_prediction
app_data['obj_date'] = obj_date
app_data['obj_id'] = obj_id
json_data = json.dumps(app_data)

#conn = httplib.HTTPSConnection("fierce-gorge-21914.herokuapp.com")
#conn.request("POST", "/new_object/" + obj_id + "/" + obj_prediction + "/" + obj_date + "/0")
#response = conn.getresponse()
#data = response.read()
#print("RESPONSE")
#print(data)
#conn.close()
webbrowser.open('https://fierce-gorge-21914.herokuapp.com/new_object/'+ obj_id + "/" + obj_prediction + "/" + obj_date + "/0")

print("JSON-DATA")
print(json_data)
