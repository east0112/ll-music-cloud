from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import os
import psycopg2
import psycopg2.extras

#postgreSQL connect関数
def get_connection():
    strCon = " user=postgres dbname= LoveLive_music password= ll0630 port= 5432 host= localhost"
    return psycopg2.connect(strCon)

#wordCloud 出力関数
def create_wordcloud(text):
    fpath = "C:\Windows\Fonts\irohamaru-Regular.ttf"
    # ストップワードの設定
    stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'', u'なっ',u'ちゃう',u'みよ',u'はず',u'なん',u'でる']

    wordCloud = WordCloud(background_color="white",font_path=fpath,  width=900, height=500, stopwords=set(stop_words)).generate(text)
    plt.figure(figsize=(15,12))
    plt.imshow(wordCloud)
    plt.axis("off")
    plt.show()

#postgreSQLへ接続
with get_connection() as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute('SELECT * FROM "music" WHERE "groupId" = 2 AND "unitId" = 7')
        musicRows = cur.fetchall()

#形態素解析 関数
def analysis_janome(text):
    t = Tokenizer()
    output = []
    for token in t.tokenize(text):
        if token.part_of_speech.split(',')[0] in ["名詞","動詞"]:
            output.append(token.surface)
    return output

#取得データの出力
text = ''
count = 0
for row in musicRows:
    strLyric = row['lyric']
    text = text + strLyric
    count = count + 1
    print('解析中：' + str(count) + '曲目')
create_wordcloud(" ".join(analysis_janome(text)))
