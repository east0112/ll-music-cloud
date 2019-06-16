import requests
import matplotlib
matplotlib.use('Agg')
from bs4 import BeautifulSoup
from flask import Flask, make_response
from urllib import parse
from common import GetConfig
from db import PostgreDAO
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer

class Plot:
    #入力の条件を基に、ワードクラウドを生成する。
    #base64でエンコードして画像情報をフロントへ返す
    def get_pic(group,unitM,unitA):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        import io
        #import random

        data = ''

        #fig, ax = matplotlib.pyplot.subplots()
        #ax.set_title(u'IMINASHI GRAPH')
        #x_ax = range(1, 284)
        #y_ax = [x * random.randint(436, 875) for x in x_ax]
        #ax.plot(x_ax, y_ax)

        #取得SQL文の作成
        get_sql = 'SELECT "musicName", "lyric" FROM "music" WHERE 1=1 '
        #グループの条件判定
        group_sql = ''
        for gr in group:
            if gr:
                group_sql =group_sql + gr +','
        if group_sql:
            #最後の文字を削除する
            group_sql = group_sql[:-1]
            #WHERE句に条件を追加する
            get_sql = get_sql + 'AND "groupId" in ({0})'
            #取得SQLへセットする
            get_sql =get_sql.format(group_sql)

        #デバッグ用
        app = Flask(__name__)
        app.logger.error(group)
        app.logger.error(get_sql)
        #DBから歌詞情報を取得する
        with PostgreDAO.get_connection() as conn:
            rows = PostgreDAO.select_data(conn,get_sql)

        #取得データの解析
        if not len(rows) == 0:
            text = ''
            count = 0
            #取得した歌詞情報連結
            for row in rows:
                strLyric = row['lyric']
                text = text + strLyric
                count = count + 1

            #ワードクラウド化
            fpath = ".irohamaru-Regular.ttf"
            # ストップワードの設定
            stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'', u'なっ',u'ちゃう',u'みよ',u'はず',u'なん',u'でる']

            #形態素解析
            t = Tokenizer()
            output = []
            for token in t.tokenize(text):
                if token.part_of_speech.split(',')[0] in ["名詞","動詞"]:
                    output.append(token.surface)
            text= " ".join(output)

            #wordCloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, stopwords=set(stop_words)).generate(text)
            wordCloud = WordCloud(background_color="white", width=900, height=500, stopwords=set(stop_words)).generate(text)

            fig = plt.figure(figsize=(12,12))
            plt.imshow(wordCloud)
            plt.axis("off")
            plt.savefig('figure.png')

            #fig = plt.figure()
            #canvas = FigureCanvasAgg(plt.subplots())
            canvas = FigureCanvasAgg(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            data = buf.getvalue()

        #base64エンコードしてhtmlに引き渡す
        responce = parse.quote(data)
        return responce
