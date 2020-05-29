import pandas as pd
from sklearn.utils import all_estimators
from sklearn.model_selection import KFold
import warnings
from sklearn.model_selection import cross_val_score

# アヤメデータの読み込み
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

# アヤメデータをラベルと入力データに分離する 
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

# classifierのアルゴリズム全てを取得する 
allAlgorithms = all_estimators(type_filter="classifier")

# K分割クロスバリデーション用オブジェクト --- (※1)
kfold_cv = KFold(n_splits=5, shuffle=True)
warnings.filterwarnings('ignore')

for(name, algorithm) in allAlgorithms :
  try :
    # 各アリゴリズムのオブジェクトを作成
    if(name == "LinearSVC") :
      clf = algorithm(max_iter = 10000)
    else:
      clf = algorithm()

    # scoreメソッドをもつクラスを対象とする--- (※2)
    if hasattr(clf,"score"):
        # クロスバリデーションを行う--- (※3)
        scores = cross_val_score(clf, x, y, cv=kfold_cv)
        print(name,"の正解率=")
        print(scores)
  
  # Exceptionは無視する
  except Exception as e :
    pass