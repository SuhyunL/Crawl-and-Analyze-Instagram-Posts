from project import db
from sqlalchemy import Column, Integer, String, PickleType


class Crawler(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    hashtag = db.Column(db.String)
    img_url = db.Column(db.String)

def __repr__(self):
    return f"hashtag: {hashtag}"