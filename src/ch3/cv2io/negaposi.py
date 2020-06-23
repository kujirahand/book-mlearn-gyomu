import matplotlib.pyplot as plt
import cv2

# 画像を読み込む
img = cv2.imread("test.jpg")
# ネガポジ反転
img = 255 - img
# 画像を表示
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
