import matplotlib.pyplot as plt
import pandas as pd

# ワインデータの読み込み
wine = pd.read_csv("winequality-white.csv", sep=";", encoding="utf-8")

# 品質データごとにグループ分けして、その数を数える
count_data = wine.groupby('quality')["quality"].count()
print(count_data)

# 数えたデータをグラフに描画
count_data.plot()
plt.savefig("wine-count-plt.png")
plt.show()

