import cv2

# 画像を読み込む
img = cv2.imread("test.jpg")

# 画像を保存する
cv2.imwrite("out.png", img)

