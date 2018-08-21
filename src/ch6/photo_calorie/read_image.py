# 画像ファイルを読んでNumpy形式に変換
import numpy as np
from PIL import Image
import os, glob, random

outfile = "image/photos.npz" # 保存ファイル名
max_photo = 100 # 利用する写真の枚数
photo_size = 32 # 画像サイズ
x = [] # 画像データ
y = [] # ラベルデータ

def main():
    # 各画像のフォルダを読む --- (*1)
    glob_files("./image/sushi", 0)
    glob_files("./image/salad", 1)
    glob_files("./image/tofu", 2)
    # ファイルへ保存 --- (*2)
    np.savez(outfile, x=x, y=y)
    print("保存しました:" + outfile, len(x))

# path以下の画像を読み込む --- (*3)
def glob_files(path, label):
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
        img = img.resize((photo_size, photo_size)) # サイズ変更
        img = np.asarray(img)
        x.append(img)
        y.append(label)

if __name__ == '__main__':
    main()
