from flask import Flask, request, jsonify
from api import *
import validators
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# API endpoint /api/colors?src=https://storage.googleapis.com/bizupimg/profile_photo/IMG_20200917_190810.jpg
# GET method will be there as we are passing the info in the form of parameter

@app.route('/api/colors',methods=['GET'])
def get_image():
    # Fetching the value src attribute
    src = request.args.get('src')
    # If we don't have any attribute like this or doesn't have any value
    if src == None or src == '':
        return "{'Error' : 404}"    
    src = src.replace(" ", "%20")
    if validators.url(src):
        # If the URL is fine, then check if the response status is correct or not ,i.e., (200 or not)
        response = requests.get(src)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            # jsonify the output, means converting the output into the json content
            return jsonify(get_colors(src))
        return "{'Error' : 404}"
    return "{'Error' : 404}"
# If somehow the URL is incorrect or isn't there then return the eror 404 in the form of JSON.

if __name__ == '__main__':
    app.run(debug = True)

