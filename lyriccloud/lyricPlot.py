import requests
import matplotlib
import io
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from bs4 import BeautifulSoup
from flask import Flask, make_response
from urllib import parse
from common import GetConfig
from db import PostgreDAO
from wordcloud import WordCloud
from common import GetConfig

#2019/06/20 DELETE START  メモリに効きすぎるため
#from janome.tokenizer import Tokenizer
#2019/06/20 DELETE END
from matplotlib.backends.backend_agg import FigureCanvasAgg

class Plot:
    #入力の条件を基に、ワードクラウドを生成する。
    #base64でエンコードして画像情報をフロントへ返す
    def get_pic(group,unit):

        #戻り値
        data = ''
        #取得SQL文の作成
        get_sql = 'SELECT \
                   "lyric_words"."word" \
                   FROM \
                   "lyric_words" \
                   INNER JOIN "music" \
                   ON "lyric_words"."music_id" = "music"."recordId" AND "lyric_words"."delete_flag" is null'

        #グループの条件判定
        group_sql = ''
        for gr in group:
            if gr:
                group_sql =group_sql + gr +','
        if group_sql:
            #最後の文字を削除する
            group_sql = group_sql[:-1]
            #WHERE句に条件を追加する
            get_sql = get_sql + ' AND "music"."groupId" in ({0})'
            #取得SQLへセットする
            get_sql =get_sql.format(group_sql)

        #ユニットの条件判定
        unit_sql = ''
        for uni in unit:
            if uni:
                unit_sql =unit_sql + uni +','
        if unit_sql:
            #最後の文字を削除する
            unit_sql = unit_sql[:-1]
            #WHERE句に条件を追加する
            get_sql = get_sql + ' AND "music"."unitId" in ({0})'
            #取得SQLへセットする
            get_sql =get_sql.format(unit_sql)

        #DBから単語情報を取得する
        with PostgreDAO.get_connection() as conn:
            rows = PostgreDAO.select_data(conn,get_sql)

        #取得データの解析
        if not len(rows) == 0:
            #取得した歌詞情報連結
            text = ''
            for row in rows:
                words = row['word']
                text = text + ' ' + words

            #ワードクラウド化
            #fpath = "irohamaru-Regular.ttf"

            fpath =  GetConfig.get_config('LyricConfig','PATH_LYRIC_FONT')
            
            # ストップワードの設定
            stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'', u'なっ',u'ちゃう',u'みよ',u'はず',u'なん',u'でる']

            #2019/06/20 DELETE START  メモリに痛恨の一撃を与えやがったため　解析後のDBを用意する
            ##形態素解析
            #t = Tokenizer()
            #output = []
            #for token in t.tokenize(text):
            #    if token.part_of_speech.split(',')[0] in ["名詞","動詞"]:
            #        output.append(token.surface)
            #text= " ".join(output)
            #2019/06/20 DELETE END

            wordCloud = WordCloud(background_color="white",font_path=fpath, width=800, height=700, colormap='rainbow',stopwords=set(stop_words)).generate(text)

            fig = plt.figure(figsize=(9,8))
            plt.imshow(wordCloud)
            plt.axis("off")

            canvas = FigureCanvasAgg(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            data = buf.getvalue()

        #base64エンコードしてhtmlに引き渡す
        responce = parse.quote(data)
        return responce
