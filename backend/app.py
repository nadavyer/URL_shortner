from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS
import string
from random import choice
import json

db = {}

def gen_code(long_url):
    chars = string.ascii_letters + string.digits
    length = 5
    code = ''.join(choice(chars) for x in range(length))
    # exists = db.session.query(
    #     db.exists().where(lon
    # g_url.new == code)).scalar()
    for car in db:
        if car == code:
            exists = True
    exists = False
    if not exists:
        return code
    code = gen_code(long_url)
    while code is None:
        code = gen_code(long_url)







app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    # if app.debug:
    #     return requests.get('http://localhost:8080/')
    return render_template("index.html")

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    request_json = request.json
    long_url = request_json['longUrl']
    code_url = gen_code(long_url)
    db[code_url] = long_url

    print long_url
    print(request_json)
    # print long_url
    return jsonify('hi from server!!')

@app.route('/<short_url>')
def get_long_url(short_url):
    return 'long_url'




if __name__ == '__main__':
    app.run(debug= True, port= '5000')
        