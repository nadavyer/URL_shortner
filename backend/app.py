from flask import Flask, render_template, jsonify, request, redirect, abort, session
from flask_cors import CORS
from random import choice
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import cast, Date, func, Time, TIME
import requests
import string
import json
import validators



    
app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class Url(db.Model):
    code_url = db.Column(db.String(10), primary_key = True)
    long_url = db.Column(db.Text, nullable = False)

class Redirects(db.Model):
    index = db.Column(db.Integer, primary_key = True, autoincrement = True)
    stat = db.Column(db.String, nullable = False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)



db.create_all()

def show_all_redirects():
    return jsonify(db.session.query(Redirects).filter(Redirects.stat == 'good').all())

def get_all_redirects_from_today():
    return db.session.query(Redirects).filter(func.date(Redirects.time_stamp) == date.today()).all()


def get_all_redirects_from_hour():
    return db.session.query(Redirects).filter(cast(Redirects.time_stamp, Time) == Time.today()).all()
    func.current


def get_all_redirects_from_hour():
    test1 = datetime.now().date()
    test2 = date.today()
    date_from_data = cast(Redirects.time_stamp, Date)
    as_func = func.date(Redirects.time_stamp)
    return db.session.query(Redirects).filter(func.date(Redirects.time_stamp) == date.today()).all()

def gen_code_for_long_url(long_url): 
    chars = string.ascii_letters + string.digits
    length = 5
    code = ''.join(choice(chars) for x in range(length))
    exist = db.session.query(
        db.exists().where(Url.code_url == code)).scalar()
    if not exist:
        return code
    code = gen_code_for_long_url(long_url)


def validate_url(long_url):
    return validators.url(long_url)

def prepare_for_url_validation(long_url):
    long_url_7_prefix = long_url[:7]
    long_url_8_prefix = long_url[:8]
    if long_url_7_prefix == 'http://' or long_url_8_prefix == 'https://':
        return long_url
    return 'http://' + long_url



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/shorten', methods = ['POST'])
def shorten_url():
    request_json = request.json
    long_url = request_json['longUrl']
    long_url = prepare_for_url_validation(long_url)
    if not validate_url(long_url):
        bad_request = Redirects(stat = 'bad')
        db.session.add(bad_request)
        db.session.commit()
        return jsonify('Not a valid URL')
    code_url = gen_code_for_long_url(long_url)
    url_to_db = Url(code_url = code_url, long_url = long_url)
    db.session.add(url_to_db)
    db.session.commit()
    return jsonify('http://localhost:5000/' + code_url)

@app.route('/api/stats', methods = ['GET'])
def send_stats_from_db():
    return jsonify(show_all_redirects())

@app.route('/<short_url>')
def get_long_url(short_url):
    exist = db.session.query(
        db.exists().where(Url.code_url == short_url)).scalar()
    if not exist:
        return  abort(404)
    ret  = db.session.query(Url).filter_by(code_url = short_url).first().long_url
    redirect_entry = Redirects( stat = 'good')
    db.session.add(redirect_entry)
    db.session.commit()
    return redirect(ret, code=302)






if __name__ == '__main__':
    app.run(debug= True, port = '5000')
        