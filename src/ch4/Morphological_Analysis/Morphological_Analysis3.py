import MeCab
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
tagger.parse("") 
# 形態素解析結果をリストで取得 --- (*1)
node = tagger.parseToNode("メイが恋ダンスを踊っている。")

result = []
while node is not None:
    # 品詞情報取得 --- (*2)
    hinshi = node.feature.split(",")[0]
    if  hinshi in ["名詞"]:
        # 表層形の取得 --- (*3)
        result.append(node.surface)
    elif hinshi in ["動詞", "形容詞"]:
        # 形態素情報から原形情報を取得 --- (*4)
        result.append(node.feature.split(",")[6])
    node = node.next
    
print(result)