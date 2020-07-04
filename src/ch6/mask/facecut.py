import cv2, dlib, sys, glob, pprint

# 入力ディレクトリの指定
indir = "./capture"
# 出力ディレクトリの指定
outdir = "./face"
# 暫定的な画像のID
fid = 1000
# 入力画像をリサイズするか？
flag_resize = False

# dlibをはじめる
detector = dlib.get_frontal_face_detector()

# 顔画像を取得して保存する
def get_face(fname):
    global fid
    img = cv2.imread(fname)
    # デジタルカメラなどの画像であれば
    # サイズが大きいのでリサイズ
    if flag_resize:
        img = cv2.resize(img, None,
            fx = 0.2, fy = 0.2)
    # 顔検出
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        pprint.pprint(d)
        x1 = int(d.left())
        y1 = int(d.top())
        x2 = int(d.right())
        y2 = int(d.bottom())
        im = img[y1:y2, x1:x2]
        # 50x50にリサイズ
        try:
            im = cv2.resize(im, (50, 50))
        except:
            continue
        # 保存
        out = outdir + "/" + str(fid) + ".jpg"
        cv2.imwrite(out, im)
        fid += 1

# ファイルを列挙して繰り返し顔検出を行う
files = glob.glob(indir+"/*")
for f in files:
    print(f)
    get_face(f)
print("ok")
