import http.client, urllib, base64
import json
from pprint import pprint
import webbrowser


#################### PREDICTION ####################
def api(image):
    pre_headers = {
        # Request headers
        'Prediction-key': '7a3c2853276a42abb5bb9c709433ec3d',
    }

    return image

    pre_params = urllib.urlencode({
        # Request parameters
        'projectId': '34a4628f-9ab4-4732-8db0-9116ff433aa5'
        })

    #with open("keypic.jpg", "rb") as imageFile:
        #f = imageFile.read()
        #body = bytearray(f)

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

        pre_json_data = json.loads(pre_data)
        obj_prediction = pre_json_data["Predictions"][0]["Tag"]
        obj_id = pre_json_data["Id"]
        obj_date = pre_json_data["Created"]

        app_data = {}
        app_data['obj_prediction'] = obj_prediction
        app_data['obj_date'] = obj_date
        app_data['obj_id'] = obj_id
        json_data = json.dumps(app_data)

        #webbrowser.open('https://fierce-gorge-21914.herokuapp.com/new_object/'+ obj_id + "/" + obj_prediction + "/" + obj_date + "/0")

        print("JSON-DATA")
        print(json_data)
        return json_data

