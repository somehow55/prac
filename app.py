from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    # return 'This is Home!'
    # return '<button>버튼데스</button>'
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

#  같은 창구(/test)지만 get을 받으면 위로, post를 받으면 아래로 간다

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/mypage')
def mypage():
    return 'This is mypage!'

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)