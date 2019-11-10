from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.debug = True

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    print(request.data)
    return jsonify('hello')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug= True)
        