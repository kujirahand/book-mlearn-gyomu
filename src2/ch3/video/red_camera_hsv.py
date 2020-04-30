import cv2
import numpy as np

# Webカメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
    # 画像を取得して縮小する
    _, frame = cap.read()
    frame = cv2.resize(frame, (500,300))
    # 色空間をHSVに変換 --- (*1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    # HSVを分割する --- (*2)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    # 赤色っぽい色を持つ画素だけを抽出 --- (*3)
    img = np.zeros(h.shape, dtype=np.uint8)
    img[((h < 50) | (h > 200)) & (s > 100)] = 255
    # ウィンドウに画像を出力 --- (*4)
    cv2.imshow('RED Camera', img)
    if cv2.waitKey(1) == 13: break

cap.release() # カメラを解放
cv2.destroyAllWindows() # ウィンドウを破棄

