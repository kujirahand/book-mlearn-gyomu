import cv2
import numpy as np

# Webカメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
    # 画像を取得
    _, frame = cap.read()
    # 画像を縮小
    frame = cv2.resize(frame, (500,300))
    r = frame[:, :, 2]
    img = np.zeros(r.shape, dtype=np.uint8)
    img[r > 120] = 255
    
    # ウィンドウに画像を出力 --- (*2)
    cv2.imshow('RED Camera', img)
    # Enterキーが押されたらループを抜ける
    if cv2.waitKey(1) == 13: break

cap.release() # カメラを解放
cv2.destroyAllWindows() # ウィンドウを破棄

