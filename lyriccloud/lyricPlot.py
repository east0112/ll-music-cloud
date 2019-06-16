import requests
import matplotlib
matplotlib.use('Agg')
from bs4 import BeautifulSoup
from flask import Flask, make_response
from urllib import parse

class Plot:
    #URLからHTMLを取得する
    #Parameters
    #url：HTMLを取得するURL
    #Returns
    #soup：html
    def get_Html(url):
        #requestsを用いてWebページのHTMLを取得する
        responceList = requests.get(url)
        responceList.status_code
        #BeautifulSoupを用いてURL要素を抽出する
        soup = BeautifulSoup(responceList.content,"lxml")
        return soup

    #HTMLから楽曲情報を抽出する
    #Parameters
    #url：HTMLを取得するURL
    #Returns
    #lyric：歌詞情報
    #music：曲名
    def get_lyric(url):
        responceList = requests.get(url)
        responceList.status_code
        #BeautifulSoupを用いてURL要素を抽出する
        soup = BeautifulSoup(responceList.content,"lxml")
        #歌詞を抽出する
        lyric = soup.find_all(id='kashi_area')
        #曲名を抽出する
        music = soup.find_all(id='ttl_name_box')

        return lyric[0].text,music[0].find('span').text.replace('曲名：','')

    #試験用
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

        #response = make_response(data)
        #response.headers['Content-Type'] = 'image/png'
        #response.headers['Content-Length'] = len(data)

        #base64エンコードしてhtmlに引き渡す
        responce = parse.quote(data)
        return responce
