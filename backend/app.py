import requests
import json

from datetime import date
from sqlalchemy import cast, Date, Time, TIME
from flask import Flask, render_template, jsonify, request, redirect, abort, session
from flask_cors import CORS

from models import db, Query, Url, Redirects, Submmit, unique_code
from utils import validate_url, long_url_from_request


def create_app(db):
    app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    db.create_all(app=app)
    return app

app = create_app(db)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/shorten', methods = ['POST'])
def shorten_url():
    long_url = long_url_from_request(request)
    validated_url = validate_url(long_url) 

    if not validated_url: 
        Submmit.add_bad_redirect(db)
        return jsonify('Not a valid URL')

    code = unique_code(db, validate_url)
    Submmit.long_short(db, code, validated_url)

    return  jsonify('http://localhost:5000/' + code)

@app.route('/api/stats', methods = ['GET'])
def send_stats_from_db():
    statistics = {
        "all_count": Query.count_all_directories(db),
        "all_good_today": Query.get_all_good_redirects_from_today(db),
         "all_good_today": Query.count_all_bad_redirects_from_today(db),
         "all_good_hour": Query.get_all_good_redirects_from_hour(db), 
         "all_bad_hour": Query.get_all_bad_redirects_from_hour(db), 
         "all_good_minute": Query.get_all_good_redirects_from_minute(db), 
         "all_bad_minute": Query.get_all_bad_redirects_from_minute(db) 
        }

    return jsonify(statistics)

@app.route('/<short_url>')
def get_long_url(short_url):
    long_url = Query.long_from_short(short_url)
    if not long_url:
        return  abort(404)        
    
    Submmit.add_successfull_redirect(db)
    return redirect(long_url, code=302)


if __name__ == '__main__':
    app.run(debug= True, port = '5000')
        