import keras
import cv2, dlib, pprint, os
import numpy as np
from keras.models import load_model

# 結果ラベル
res_labels = ['NO MASK!!', 'ok']
save_dir = "./live"

# 保存した学習データを読む --- (※1)
model = load_model('mask_model.h5')

# Dlibをはじめる --- (※2)
detector = dlib.get_frontal_face_detector()

# Webカメラから入力を開始 --- (※3)
red = (0,0,255)
green = (0, 255, 0)
fid = 1
cap = cv2.VideoCapture(0)
while True:
    # カメラの画像を読み込む --- (※4)
    ok, frame = cap.read()
    if not ok: break
    # 画像を縮小表示する --- (※5)
    frame = cv2.resize(frame, (500,300))
    # 顔検出 --- (※6)
    dets = detector(frame, 1)
    for k, d in enumerate(dets):
        pprint.pprint(d)
        x1 = int(d.left())
        y1 = int(d.top())
        x2 = int(d.right())
        y2 = int(d.bottom())
        # 顔部分を切り取る --- (※7)
        im = frame[y1:y2, x1:x2]
        im = cv2.resize(im, (50, 50))
        im = im.reshape(-1, 50, 50, 3)
        # 予測 --- (※8)
        res = model.predict([im])[0]
        v = res.argmax()
        print(res_labels[v], res)
        # 枠を描画 --- (※9)
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
    if len(dets) > 0: # 結果を保存
        if os.path.exists(save_dir):
            jpgfile = save_dir + "/" + str(fid) + ".png"
            cv2.imwrite(jpgfile, frame)
            fid += 1
    # ウィンドウに画像を出力 --- (※10)
    cv2.imshow('Mask Live Check', frame)
    # ESCかEnterキーが押されたらループを抜ける
    k = cv2.waitKey(1) # 1msec確認
    if k == 27 or k == 13: break

cap.release() # カメラを解放
cv2.destroyAllWindows() # ウィンドウを破棄
