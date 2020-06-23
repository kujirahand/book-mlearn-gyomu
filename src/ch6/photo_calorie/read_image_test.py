# 画像ファイルを読んでNumpy形式に変換
import numpy as np
from PIL import Image
import os, glob, random

outfile = "image/photos.npz" # 保存ファイル名
max_photo = 100 # 利用する写真の枚数
photo_size = 32 # 画像サイズ
X = [] # 画像データ
y = [] # ラベルデータ

# path以下の画像を最大max_photoだけ読む --- (*1)
def glob_files(path, label, max_photo):
    files = glob.glob(path + "/*.jpg")
    random.shuffle(files)
    # 各ファイルを処理
    num = 0
    for f in files:
        if num >= max_photo: break
        num += 1
        # 画像ファイルを読む
        img = Image.open(f)
        img = img.convert("RGB") # 色空間をRGBに
        img = img.resize((photo_size, photo_size))
        X.append(image_to_data(img))
        y.append(label)
        # 角度を少しずつ変えた画像を追加 --- (*2)
        for angle in range(-20, 21, 5):
            # 角度を変更
            if angle != 0:
                img_angle = img.rotate(angle)
                X.append(image_to_data(img_angle))
                y.append(label)
            # 反転
            img_r = img_angle.transpose(Image.FLIP_LEFT_RIGHT)
            X.append(image_to_data(img_r))
            y.append(label)

def image_to_data(img): # 画像データを正規化
    data = np.asarray(img)
    data = data / 256
    data = data.reshape(photo_size, photo_size, 3)
    return data

# 各画像のフォルダを読む --- (*3)
glob_files("./image/sushi", 0, max_photo)
glob_files("./image/salad", 1, max_photo)
glob_files("./image/tofu", 2, max_photo)

# ファイルへ保存 --- (*4)
X = np.array(X, dtype=np.float32)
np.savez(outfile, X=X, y=y)
print("保存しました:" + outfile)
