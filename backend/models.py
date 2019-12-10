from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time, timedelta
from sqlalchemy import func

from utils import gen_code_for_long_url


db = SQLAlchemy()

class Url(db.Model):
    code_url = db.Column(db.String(10), primary_key = True)
    long_url = db.Column(db.Text, nullable = False)


class Redirects(db.Model):
    index = db.Column(db.Integer, primary_key = True, autoincrement = True)
    stat = db.Column(db.String, nullable = False)
    time_stamp = db.Column(db.DateTime, default=datetime.now())


class Submmit:

    @staticmethod
    def add_log(db, status):
        entry = Redirects(stat=status)
        db.session.add(entry)
        db.session.commit()

    @staticmethod
    def add_successfull_redirect(db):
        Submmit.add_log(db, "good")

    @staticmethod
    def add_bad_redirect(db):
        Submmit.add_log(db, "bad")

    @staticmethod
    def long_short(db, code, long_url):
        url_to_db = Url(code_url=code, long_url=long_url)
        db.session.add(url_to_db)
        db.session.commit()


class Query:

    @staticmethod
    def count_all_redirects(db):
        return db.session.query(func.count(Redirects.stat)).filter(Redirects.stat == 'good').scalar()

    @staticmethod
    def get_all_good_redirects_from_today(db):
        return db.session.query(func.count(Redirects.stat)).filter(func.date(Redirects.time_stamp) == date.today(),
                                                                     Redirects.stat == 'good').scalar()
        
    @staticmethod
    def count_all_bad_redirects_from_today(db):
        return db.session.query(func.count(Redirects.stat)).filter(func.date(Redirects.time_stamp) == date.today(),
                                                                     Redirects.stat == 'bad').scalar()

    @staticmethod
    def get_all_good_redirects_from_hour(db):
        since = datetime.now() - timedelta(hours=1)
        return db.session.query(func.count(Redirects.stat)).filter(Redirects.time_stamp >= since,
                                                                     Redirects.stat == 'good').scalar()
    
    @staticmethod
    def get_all_bad_redirects_from_hour(db):
        since = datetime.now() - timedelta(hours=1)
        return db.session.query(func.count(Redirects.stat)).filter(Redirects.time_stamp >= since,
                                                                     Redirects.stat == 'bad').scalar()

    @staticmethod
    def get_all_good_redirects_from_minute(db):
        since = datetime.now() - timedelta(minutes=1)
        return db.session.query(func.count(Redirects.stat)).filter(Redirects.time_stamp >= since,
                                                                     Redirects.stat == 'good').scalar()
    @staticmethod
    def get_all_bad_redirects_from_minute(db):
        since = datetime.now() - timedelta(minutes=1)
        return db.session.query(func.count(Redirects.stat)).filter(Redirects.time_stamp >= since,
                                                                    Redirects.stat == 'bad').scalar()
    

    @staticmethod
    def long_from_short(short_url):
        exist = db.session.query(
        db.exists().where(Url.code_url == short_url)).scalar()
        
        if not exist:
            return  None

        return db.session.query(Url).filter_by(code_url = short_url).first().long_url

    @staticmethod
    def code_exists(db, code):
        exist = db.session.query(db.exists().where(Url.code_url == code)).scalar()
        return exist


def unique_code(db, url):
    code_url = gen_code_for_long_url(url)
    while Query.code_exists(db, code_url):
        code_url = gen_code_for_long_url(validated_url)

    return code_url
