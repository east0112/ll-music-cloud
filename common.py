from flask import Flask

class GetConfig:
    #クラス名、キー情報を基に設定値を取得する
    #Parameters
    #class：設定値が定義されたクラス
    #key：設定値のキー
    #Returns
    #：html
    def get_config(classStr,key):
        classStr = 'config.' + classStr
        app = Flask(__name__)
        app.config.from_object(classStr)
        text = app.config[key]
        return text
