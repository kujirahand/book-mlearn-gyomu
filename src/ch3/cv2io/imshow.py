# ダウンロードした画像を画面に表示する
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("test.jpg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

