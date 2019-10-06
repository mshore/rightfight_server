from flask import request
from app.models import LBoardRecord
from app import app
from app import db
import sqlite3
import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/detroitsmash')
def addtoleaderboard():
    params = request.args
    uuid = params["uuid"]
    uname = params["uname"]
    end_score = params["score"]
    if not uname or not end_score: return
    rec = LBoardRecord(id=uuid, name=uname, score=int(end_score))
    db.session.add(rec)
    db.session.commit()
    return "no one cares"



