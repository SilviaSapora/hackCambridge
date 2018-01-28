import os
from flask import Flask, request
from flask_restful import Resource, Api
import json
from json import dumps
from flask import send_file
import prediction

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
    def get(self, image):
        print(image)
        prediction.api(image)        
        return send_file(filename, mimetype='image')

api.add_resource(Picture, '/picture/<string:image>')

if __name__ == '__main__':
     app.run()
