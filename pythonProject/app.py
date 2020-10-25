from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def make_order():
    name_receive = request.form['name_give']
    qty_receive = request.form['qty_give']
    add_receive = request.form['add_give']
    pn_receive = request.form['pn_give']
    # 2. DB에 정보 삽입하기

    doc = {
        'name': name_receive,
        'qty': qty_receive,
        'add': add_receive,
        'pn': pn_receive,
    }

    db.myorders.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다~'})


@app.route('/order', methods=['GET'])
def receive_order():
    orders = list(db.myorders.find({}, {'_id':False}))
    return jsonify({'result': 'success', 'orders': 'orders'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
