import keras
import cv2, dlib, pprint, os, sys
import numpy as np
from keras.models import load_model

# 結果ラベル
res_labels = ['NO MASK!!', 'ok']

# 保存した学習データを読む 
model = load_model('mask_model.h5')

# 写真から入力を
if len(sys.argv) <= 1:
    print("[USAGE] photo_check.py infile.jpg")
    quit()
fname = sys.argv[1]
frame = cv2.imread(fname)
# 横幅が500pxになるようリサイズ
width = 500
h, w = frame.shape[:2]
height = round(h * (width / w))
frame = cv2.resize(frame, dsize=(width, height))

# 顔検出
red = (0,0,255)
green = (0, 255, 0)
detector = dlib.get_frontal_face_detector()
dets = detector(frame, 1)
for k, d in enumerate(dets):
    pprint.pprint(d)
    x1 = int(d.left())
    y1 = int(d.top())
    x2 = int(d.right())
    y2 = int(d.bottom())
    # 顔部分を切り取る
    im = frame[y1:y2, x1:x2]
    im = cv2.resize(im, (50, 50))
    im = im.reshape(-1, 50, 50, 3)
    # 予測 
    res = model.predict([im])[0]
    v = res.argmax()
    print(res_labels[v], res)
    # 枠を描画
    color = green if v == 1 else red
    border = 2 if v == 1 else 7
    cv2.rectangle(frame, 
      (x1, y1), (x2, y2), color, 
      thickness=border)
    # テキストを描画
    cv2.putText(frame,
        res_labels[v], (x1, y1-7),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9, color, thickness=2)

jpgfile = fname + "-out.png"
cv2.imwrite(jpgfile, frame)

