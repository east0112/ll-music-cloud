from flask import Flask

# Flask の起動
app = Flask(__name__)

from lyriccloud.views import lyriccloud
app.register_blueprint(lyriccloud, url_prefix='/lyriccloud')

## ルートにアクセスしたときに実行される関数
#@app.route('/')
#def index():
#    return render_template('wordcloud\templates\index.html')

app.run(host="localhost")
