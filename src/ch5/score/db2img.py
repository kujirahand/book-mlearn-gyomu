# ETL1Cのファイルを読み込む
import struct
from PIL import Image, ImageEnhance
import glob, os

# 出力ディレクトリ
outdir = "png-etl1/"
if not os.path.exists(outdir): os.mkdir(outdir)

# ETL1ディレクトリ以下のファイルを処理する --- (*1)
files = glob.glob("ETL1/*")
for fname in files:
    if fname == "ETL1/ETL1INFO": continue # 情報ファイルは飛ばす
    print(fname)
    # ETL1のデータファイルを開く --- (*2)
    f = open(fname, 'rb')
    f.seek(0)
    while True:
        # メタデータ＋画像データの組を一つずつ読む --- (*3)
        s = f.read(2052)
        if not s: break
        # バイナリデータなのでPythonが理解できるように抽出 --- (*4)
        r = struct.unpack('>H2sH6BI4H4B4x2016s4x', s)
        code_ascii = r[1]
        code_jis = r[3]
        # 画像データとして取り出す --- (*5)
        iF = Image.frombytes('F', (64, 63), r[18], 'bit', 4)
        iP = iF.convert('L')
        # 画像を鮮明にして保存
        dir = outdir + "/" + str(code_jis)
        if not os.path.exists(dir): os.mkdir(dir)
        fn = "{0:02x}-{1:02x}{2:04x}.png".format(code_jis, r[0], r[2])
        fullpath = dir + "/" + fn
        #if os.path.exists(fullpath): continue
        enhancer = ImageEnhance.Brightness(iP)
        iE = enhancer.enhance(16)
        iE.save(fullpath, 'PNG')
print("ok")
