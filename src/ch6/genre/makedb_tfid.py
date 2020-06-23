import os, glob, pickle
import tfidf

# 変数の初期化
y = []
x = []

# ディレクトリ内のファイル一覧を処理 --- (*1)
def read_files(path, label):
    print("read_files=", path)
    files = glob.glob(path + "/*.txt")
    for f in files:
        if os.path.basename(f) == 'LICENSE.txt': continue
        tfidf.add_file(f)
        y.append(label)

# ファイル一覧を読む --- (*2)
read_files('text/sports-watch', 0)
read_files('text/it-life-hack', 1)
read_files('text/movie-enter', 2)
read_files('text/dokujo-tsushin', 3)

# TF-IDFベクトルに変換 --- (*3)
x = tfidf.calc_files()

# 保存 --- (*4)
pickle.dump([y, x], open('text/genre.pickle', 'wb'))
tfidf.save_dic('text/genre-tdidf.dic')
print('ok')
