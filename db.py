#データベース接続モジュール
import os
import psycopg2
import psycopg2.extras
from common import GetConfig
from flask import Flask

class PostgreDAO:
    #PostgreSQL接続クラス

    #postgreSQL connect関数
    def get_connection(strCon):

        user =  GetConfig.get_config('DataBaseConfig','SQL_DATABASE_USER')
        dbname =  GetConfig.get_config('DataBaseConfig','SQL_DATABASE_NAME')
        password =  GetConfig.get_config('DataBaseConfig','SQL_DATABASE_PASS')
        port =  GetConfig.get_config('DataBaseConfig','SQL_DATABASE_PORT')
        host =  GetConfig.get_config('DataBaseConfig','SQL_DATABASE_HOST')
        strCon = ' user={0} dbname={1} password={2} port={3} host={4}'
        return psycopg2.connect(strCon.format(user,dbname,password,port,host))

    #postgreSQL select関数
    def select_data():
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('SELECT * FROM "music" WHERE "groupId" = 2 AND "unitId" = 7')
            musicRows = cur.fetchall()
        return musicRows
