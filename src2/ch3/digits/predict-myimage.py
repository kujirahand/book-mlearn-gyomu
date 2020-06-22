import cv2
import pickle

def predict_digit(filename):
    # 学習済みデータを読み込む
    with open("digits.pkl", "rb") as fp:
        clf = pickle.load(fp)
    # 自分で用意した手書きの画像ファイルを読み込む
    my_img = cv2.imread(filename)
    # 画像データを学習済みデータに合わせる
    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
    my_img = cv2.resize(my_img, (8, 8))
    my_img = 15 - my_img // 16 # 白黒反転する
    # 二次元を一次元に変換
    my_img = my_img.reshape((-1, 64))
    # データ予測する
    res = clf.predict(my_img)
    return res[0]

# 画像ファイルを指定して実行
n = predict_digit("my2.png")
print("my2.png = " + str(n))
n = predict_digit("my4.png")
print("my4.png = " + str(n))
n = predict_digit("my9.png")
print("my9.png = " + str(n))
