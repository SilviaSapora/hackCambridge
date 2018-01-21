from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import send_file


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Yo, it's working!"

class Objects(Resource):
    def get(self):
        with open('../objects.txt', 'r') as myfile:
            data = myfile.read()
        print(data)

        return data

class Picture(Resource):
    def get(self, obj_id):
        filename = "image" + obj_id + ".jpg"
        return send_file(filename, mimetype='image')
 
api.add_resource(Objects, '/obj')
api.add_resource(Picture, '/picture/<string:obj_id>')

if __name__ == '__main__':
     app.run()
