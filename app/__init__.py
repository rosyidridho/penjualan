from flask import Flask, g
from .config import data_json, BASE, STATIC_PATH, status
import MySQLdb, os

app = Flask(__name__)

app.secret_key = 'PENJUALAN'

@app.context_processor
def app_info():
    data = {
        "app_name": data_json["app_name"],
        "description": data_json["description"],
        "version": data_json["version"],
        "status": data_json["status"]
    }
    return dict(app_info=data)

@app.before_request
def db_connect():
    g.conn = MySQLdb.connect(
        host = data_json["db"]["db_host"],
        user = data_json["db"]["db_user"],
        passwd = data_json["db"]["db_password"],
        db = data_json["db"]["db_name"],
        charset = 'utf8',
        use_unicode = True
    )
    g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
    g.cursor.close()
    g.conn.close()
    return response

if status == 'development':
    app.static_folder = os.path.join(BASE, 'static')
elif status == 'production':
    app.static_folder = STATIC_PATH

from .urls import *
from .errors import *