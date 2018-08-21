import cv2
import numpy as np

# Webカメラから入力を開始 --- (*1)
cap = cv2.VideoCapture(0)
while True:
    # カメラの画像を読み込む --- (*2)
    _, frame = cap.read()
    # 画像を縮小表示する --- (*3)
    frame = cv2.resize(frame, (500,300))
    # ウィンドウに画像を出力 --- (*4)
    cv2.imshow('OpenCV Web Camera', frame)
    # ESCかEnterキーが押されたらループを抜ける
    k = cv2.waitKey(1) # 1msec確認
    if k == 27 or k == 13: break

cap.release() # カメラを解放
cv2.destroyAllWindows() # ウィンドウを破棄

