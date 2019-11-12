from extensions import db

class Link(db.Model):
    short_url = db.Column(db.Integer, primary_key = True)