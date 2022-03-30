
from flask import Flask
from .bluePrints.monitor import mon
from .bluePrints.arquivos import api_arq
from .bluePrints.cliente import client
from .model import Arquivos

from sqlalchemy.event import listens_for
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection


app = Flask(__name__)
app.config.from_object('config')
Arquivos.db.init_app(app)
Arquivos.ma.init_app(app)


app.register_blueprint(mon)
app.register_blueprint(api_arq)
app.register_blueprint(client)

from .bluePrints.initial import root_send_file


@listens_for(Engine, "connect")
def my_on_connect(dbapi_con, connection_record):
    if isinstance(dbapi_con, SQLite3Connection):
        cursor = dbapi_con.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


with app.app_context():
    Arquivos.db.create_all()
