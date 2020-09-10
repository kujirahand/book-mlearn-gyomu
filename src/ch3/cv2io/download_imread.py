# 画像のダウンロード
import urllib.request as req
url = "https://uta.pw/shodou/img/28/214.png"
req.urlretrieve(url, "test.png")

# OpenCVで読み込む
import cv2
img = cv2.imread("test.png")
print(img)

