import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle

# 保存先や画像サイズの指定 --- (*1)
out_dir = "./png-etl1" # 画像データがあるディレクトリ
im_size = 25 # 画像サイズ
save_file = out_dir + "/katakana.pickle" # 保存先
plt.figure(figsize=(9, 17)) # 出力画像を大きくする

# カタカナの画像が入っているディレクトリから画像を取得 --- (*2)
kanadir = list(range(177, 220+1))
kanadir.append(166) # ヲ
kanadir.append(221) # ン
result = []
for i, code in enumerate(kanadir):
    img_dir = out_dir + "/" + str(code)
    fs = glob.glob(img_dir + "/*")
    print("dir=",  img_dir)
    # 画像を読み込んでグレイスケールに変換しリサイズする --- (*3)
    for j, f in enumerate(fs):
        img = cv2.imread(f)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img_gray, (im_size, im_size))
        result.append([i, img])
        # Jupyter Notebookで画像を出力
        if j == 3:
            plt.subplot(11, 5, i + 1)
            plt.axis("off")
            plt.title(str(i))
            plt.imshow(img, cmap='gray')
# ラベルと画像のデータを保存 --- (*4)
pickle.dump(result, open(save_file, "wb"))
plt.show()
print("ok")
