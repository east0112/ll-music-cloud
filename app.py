import os
from flask import Flask

# Flask の起動
application = Flask(__name__)
application.config.from_object("config.DataBaseConfig")

from lyriccloud.views import lyriccloud
application.register_blueprint(lyriccloud, url_prefix='/lyriccloud')

## ルートにアクセスしたときに実行される関数
#@app.route('/')
#def index():
#    return render_template('wordcloud\templates\index.html')

#print(app.config['SQL_DATABASE_USER'])
#app.run(host="localhost",debug=True)
#app.run(host='0.0.0.0',debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0',port=port)
