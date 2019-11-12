from extensions import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key = True)