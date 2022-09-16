from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient(
    'mongodb://test:sparta@ac-qs2cnvy-shard-00-00.u33zjtg.mongodb.net:27017,ac-qs2cnvy-shard-00-01.u33zjtg.mongodb.net:27017,ac-qs2cnvy-shard-00-02.u33zjtg.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-4g7ly1-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})


@app.route("/worldlikesTOTAL", methods=["GET"])
def wlT_get():
    wlT_list = list(db.worldlikesTOTAL.find({}, {'_id': False}))
    return jsonify({'wlT': wlT_list})

@app.route("/worldviewsMONTHLY", methods=["GET"])
def wvM_get():
    wvM_list = list(db.worldviewsMONTHLY.find({}, {'_id': False}))
    return jsonify({'wvM': wvM_list})

@app.route("/worldviewsTOTAL", methods=["GET"])
def wvT_get():
    wvT_list = list(db.worldviewsTOTAL.find({}, {'_id': False}))
    return jsonify({'wvT': wvT_list})

@app.route("/worldviewsWEEKLY", methods=["GET"])
def wvW_get():
    wvW_list = list(db.worldviewsWEEKLY.find({}, {'_id': False}))
    return jsonify({'wvW': wvW_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)