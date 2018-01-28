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

@app.route('/picture', methods=['GET', 'POST'])
def API():
    #print(image)
    return request.getData()        

api.add_resource(Picture, '/picture/<string:image>')

if __name__ == '__main__':
     app.run()
