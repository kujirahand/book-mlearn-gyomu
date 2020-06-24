# ジャンケンデータを作成する
import pickle
import numpy as np

# ジャンケンの手と結果を定義 --- (*1)
hands = {'グー':0, 'チョキ':1, 'パー':2}
results = ['あいこ', '負け', '勝ち']

# じゃんけんの公式を定義 --- (*2)
judge = lambda a, b: (a - b + 3) % 3

# ランダムにデータを作成 --- (*3)
import random
random_hand = lambda : random.randint(0, 2)
x_items = []
y_items = []
for i in range(3000):
    a = random_hand()
    b = random_hand()
    result = judge(a, b)
    x_items.append([a, b])
    y_items.append(result)
# 作成したデータを表示
print(x_items)
print(y_items)

# データを学習用とテスト用に分割 --- (*4)
x_train = x_items[0:2000]
y_train = y_items[0:2000]
x_test = x_items[2000:]
y_test = y_items[2000:]
# データを保存 --- (*5)
items = [[x_train, y_train],
        [x_test, y_test]]
with open("janken-data.pkl", "wb") as fp:
    pickle.dump(items, fp)
    
