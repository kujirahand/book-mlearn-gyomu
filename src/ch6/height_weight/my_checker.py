from keras.models import load_model
import numpy as np

# 学習モデルを読み込む --- (*1)
model = load_model('hw_model.h5')
# 学習済みデータを読み込む --- (*2)
model.load_weights('hw_weights.h5')
# ラベル
LABELS = [
    '低体重(痩せ型)', '普通体重', '肥満(1度)', 
    '肥満(2度)', '肥満(3度)', '肥満(4度)'
]

# テストデータを指定 --- (*3)
height = 160
weight = 50
# 0-1の範囲に収まるようにデータを正規化 --- (*4)
test_x = [height / 200, weight / 150]
# 予測 --- (*5)
pre = model.predict(np.array([test_x]))
idx = pre[0].argmax()
print(LABELS[idx], '/可能性', pre[0][idx])

