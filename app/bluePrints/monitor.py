import configparser
import os
from flask import Blueprint, jsonify


cfg = configparser.ConfigParser()
cfg.read('CONFIG.ini')


DIRETORIO = cfg.get("DIRETORIO", "CAMINHO")


mon = Blueprint('mon', __name__)


@mon.route('/Monitor', methods=['GET'])
def monitor_rout():
    return jsonify({'msg': f'{os.listdir(DIRETORIO)}'})