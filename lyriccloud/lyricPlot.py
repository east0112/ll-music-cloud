import requests
import matplotlib
matplotlib.use('Agg')
from bs4 import BeautifulSoup
from flask import Flask, make_response
from urllib import parse
from common import GetConfig

class Plot:
    #入力の条件を基に、ワードクラウドを生成する。
    #base64でエンコードして画像情報をフロントへ返す
    def get_pic():
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

        #実験用
        afafa = GetConfig.get_config('DataBaseConfig','SQL_DATABASE_USER')
        #base64エンコードしてhtmlに引き渡す
        responce = parse.quote(data)
        return responce
