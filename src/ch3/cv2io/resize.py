import matplotlib.pyplot as plt
import cv2

# 画像を読み込む
img = cv2.imread("test.jpg")
# 画像をリサイズ
im2 = cv2.resize(img, (600, 300))
# リサイズした画像を保存
cv2.imwrite("out-resize.png", im2)

# 画像を表示
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()
