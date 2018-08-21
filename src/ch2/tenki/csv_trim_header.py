in_file = "data.csv"
out_file = "kion10y.csv"

# CSVファイルを一行ずつ読み込み ---(*1)
with open(in_file, "rt", encoding="Shift_JIS") as fr:
    lines = fr.readlines()

# ヘッダをそぎ落として、新たなヘッダをつける ---(*2)
lines = ["年,月,日,気温,品質,均質\n"] + lines[5:]
lines = map(lambda v: v.replace('/', ','), lines)
result = "".join(lines).strip()
print(result)

# 結果をファイルへ出力 ---(*3)
with open(out_file, "wt", encoding="utf-8") as fw:
    fw.write(result)
    print("saved.")
