import requests
import matplotlib
matplotlib.use('Agg')
from bs4 import BeautifulSoup
from flask import Flask, make_response
from urllib import parse
from common import GetConfig
from db import PostgreDAO

class Plot:
    #入力の条件を基に、ワードクラウドを生成する。
    #base64でエンコードして画像情報をフロントへ返す
    def get_pic(group,unitM,unitA):
        import matplotlib.pyplot
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        import io
        import random

        fig, ax = matplotlib.pyplot.subplots()
        ax.set_title(u'IMINASHI GRAPH')
        x_ax = range(1, 284)
        y_ax = [x * random.randint(436, 875) for x in x_ax]
        ax.plot(x_ax, y_ax)

        canvas = FigureCanvasAgg(fig)
        buf = io.BytesIO()
        canvas.print_png(buf)
        data = buf.getvalue()

        #取得SQL文の作成
        get_sql = 'SELECT "musicName", "lyric" FROM "music" WHERE 1=1 '
        #グループの条件判定
        group_sql = ''
        for gr in group:
            if gr:
                group_sql =group_sql + gr +','
            #group_sql =group_sql + gr +',' if gr else group_sql =group_sql
        if group_sql:
            #最後の文字を削除する
            group_sql = group_sql[:-1]
            #WHERE句に条件を追加する
            get_sql = get_sql + 'AND "groupId" in ({0})'
            #取得SQLへセットする
            get_sql =get_sql.format(group_sql)

        #デバッグ用
        #app = Flask(__name__)
        #app.logger.error(group)
        #app.logger.error(get_sql)
        #DBから歌詞情報を取得する
        with PostgreDAO.get_connection() as conn:
            rows = PostgreDAO.select_data(get_sql)

        #取得データの解析



        #base64エンコードしてhtmlに引き渡す
        responce = parse.quote(data)
        return responce
