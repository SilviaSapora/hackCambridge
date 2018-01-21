import os
from flask import Flask, request
from flask_restful import Resource, Api
import json
from json import dumps
from flask import send_file


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Yo, it's working!"

class Objects(Resource):
    def get(self):
        with open('obj.txt', 'r') as myfile:
            data = myfile.read()
        print(data)

        return data

class Picture(Resource):
    def get(self, obj_id):
        filename = "image" + obj_id + ".jpg"
        return send_file(filename, mimetype='image')

class Upload(Resource):
    def get(self, obj_id, obj_prediction, obj_date, obj_exp):
        with open("obj.txt", "rb") as obj_file:
            f = obj_file.read()
            jsobj = json.loads(f)
        app_data = {}
        app_data['obj_exp'] = obj_exp
        app_data['obj_prediction'] = obj_prediction
        app_data['obj_date'] = obj_date
        app_data['obj_id'] = obj_id
        json_data = json.dumps(app_data)
        jsobj["objects"].append(app_data)
        file_updated_data = json.dumps(jsobj)
        os.remove("obj.txt")
        with open('obj.txt', 'a') as the_file:
            the_file.write(file_updated_data)
        return "Uploaded successfully!"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/<string:filename>', methods=['GET', 'POST'])
def upload_file(filename):
    if request.method == 'POST':
            file.save(os.path.join(filename))
            return "File uploaded successfully"

api.add_resource(Upload, '/new_object/<string:obj_id>/<string:obj_prediction>/<string:obj_date>/<string:obj_exp>')
api.add_resource(Objects, '/obj')
api.add_resource(Picture, '/picture/<string:obj_id>')

if __name__ == '__main__':
     app.run()
