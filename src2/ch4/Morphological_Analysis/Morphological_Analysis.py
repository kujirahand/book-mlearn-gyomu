import MeCab
# MeCabオブジェクトの生成 --- (*1)
tagger = MeCab.Tagger()
# 形態素解析 --- (*2)
result = tagger.parse("メイが恋ダンスを踊っている。")
print(result)