import matplotlib.pyplot as plt
import pandas as pd
# CSVを読み込む ---(*1)
df = pd.read_csv("kion10y.csv", encoding="utf-8")
# 月ごとに平均を求める ---(*2)
g = df.groupby(['月'])["気温"]
gg = g.sum() / g.count()
# 結果を出力 ---(*3)
print(gg)
gg.plot()
plt.savefig("tenki-heikin-tuki.png")
plt.show()

