from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://b1team:intro@zelda.oqyai4s.mongodb.net/?retryWrites=true&w=majority')
db = client.b1team

from bson.json_util import dumps

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('main.html') 
# 우선 메인페이지 연결함

@app.route('/page2')
def page2():
    return render_template('page2.html') 

@app.route('/teamcard')
def team():
    return render_template('teamcard.html') 

@app.route("/ayintro", methods=["POST"])
def ayintro_post():
    aycomment_receive = request.form['aycomment_give']
    doc = {
        'aycomment':aycomment_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'아영님께 댓글 남기기 완료!'})

@app.route("/jwintro", methods=["POST"])
def jwintro_post():
    jwcomment_receive = request.form['jwcomment_give']

    doc = {
        'jwcomment':jwcomment_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'종우님께 댓글 남기기 완료!'})

@app.route("/jsintro", methods=["POST"])
def jsintro_post():
    jscomment_receive = request.form['jscomment_give']

    doc = {
        'jscomment':jscomment_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'지수님께 댓글 남기기 완료!'})

@app.route("/jhintro", methods=["POST"])
def jhintro_post():
    jhcomment_receive = request.form['jhcomment_give']

    doc = {
        'jhcomment':jhcomment_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'진희님께 댓글 남기기 완료!'})

@app.route("/jmintro", methods=["POST"])
def jmintro_post():
    jmcomment_receive = request.form['jmcomment_give']

    doc = {
        'jmcomment':jmcomment_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg':'주민님께 댓글 남기기 완료!'})

@app.route("/ayintro", methods=["GET"])
def ayintro_get():
    all_aycomments = list(db.comment.find({"aycomment": {"$exists": True}}))
    result=dumps(all_aycomments)
    return jsonify({'result':result})

@app.route("/jwintro", methods=["GET"])
def jwintro_get():
    all_jwcomments = list(db.comment.find({"jwcomment": {"$exists": True}}))
    result=dumps(all_jwcomments)
    return jsonify({'result':result})

@app.route("/jsintro", methods=["GET"])
def jsintro_get():
    all_jscomments = list(db.comment.find({"jscomment": {"$exists": True}}))
    result=dumps(all_jscomments)
    return jsonify({'result':result})

@app.route("/jhintro", methods=["GET"])
def jhintro_get():
    all_jhcomments = list(db.comment.find({"jhcomment": {"$exists": True}}))
    result=dumps(all_jhcomments)
    return jsonify({'result':result})

@app.route("/jmintro", methods=["GET"])
def jmintro_get():
    all_jmcomments = list(db.comment.find({"jmcomment": {"$exists": True}}))
    result=dumps(all_jmcomments)
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)