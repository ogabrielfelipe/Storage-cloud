import os
import configparser

cfg = configparser.ConfigParser()
cfg.read('CONFIG.ini')

DB = os.path.abspath(cfg.get("DIRETORIO", "DB"))

DEBUG=True
SQLALCHEMY_DATABASE_URI = f'sqlite+pysqlite:///{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
