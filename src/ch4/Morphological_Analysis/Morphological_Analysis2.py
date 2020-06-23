import MeCab
# mecab-ipadic-NEologd辞書を指定して、MeCabオブジェクトの生成 --- (*1)
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
# 形態素解析
result = tagger.parse("メイが恋ダンスを踊っている。")
print(result)