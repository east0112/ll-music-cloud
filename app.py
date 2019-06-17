from flask import Flask

# Flask の起動
app = Flask(__name__)
app.config.from_object("config.DataBaseConfig")

from lyriccloud.views import lyriccloud
app.register_blueprint(lyriccloud, url_prefix='/lyriccloud')

## ルートにアクセスしたときに実行される関数
#@app.route('/')
#def index():
#    return render_template('wordcloud\templates\index.html')

#print(app.config['SQL_DATABASE_USER'])
#app.run(host="localhost",debug=True)
app.run(host='0.0.0.0',debug=True)
