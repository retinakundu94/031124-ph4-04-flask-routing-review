#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db , Meme # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"


# write your routes here!

@app.get('/meme-table')
def get_memes():
    return [m.to_dict() for m in Meme.query.all()]

@app.post('/meme-table')
def post_memes():
    new_memes = Meme(img_url=request.json['img_url'], caption=request.json['caption'])

    db.session.add(new_memes)
    db.session.commit()

    return new_memes.to_dict(), 201

@app.patch('/meme-table/<int:id>')
def patch_rqst(id:int):
    meme_table_to_update = Meme.query.where(Meme.id == id).first()

    if meme_table_to_update:
       for key in request.json.keys():
    
        setattr(meme_table_to_update, key, request.json[key])

        db.session.add(meme_table_to_update)
        db.session.commit()

        return meme_table_to_update.to_dict(), 202
       
    else:
        return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
