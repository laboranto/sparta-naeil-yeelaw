from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://justavojo:h9BuPyN2TgFWsx5@cluster0.r98ilu0.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']

    doc = {'nickname': nickname_receive, 'comment': comment_receive}
    db.fanlog.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_fans = list(db.fanlog.find({}, {'_id': False}))
    return jsonify({'fanlog':all_fans})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)