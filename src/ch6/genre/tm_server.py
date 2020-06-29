import json
import flask
from flask import request
import my_text

# ポート番号 --- (*1)
TM_PORT_NO = 8888
# HTTPサーバを起動
app = flask.Flask(__name__)

# 一度、ジャンル判定のテストをする
label, per, no = my_text.check_genre("テスト")
print("> テスト --- ", label, per, no)

# ルートへアクセスした場合 --- (*2)
@app.route('/', methods=['GET'])
def index():
    with open("index.html", "rb") as f:
        return f.read()

# /api へアクセスした場合
@app.route('/api', methods=['GET'])
def api():
    # URLパラメータを取得 --- (*3)
    q = request.args.get('q', '')
    if q == '':
      return '{"label": "空です", "per":0}'
    print("q=", q)
    # テキストのジャンル判定を行う --- (*4)
    label, per, no = my_text.check_genre(q)
    # 結果をJSONで出力
    return json.dumps({
      "label": label, 
      "per": per,
      "genre_no": no
    })
    
if __name__ == '__main__':
    # サーバを起動
    app.run(debug=True, host='0.0.0.0', port=TM_PORT_NO)

