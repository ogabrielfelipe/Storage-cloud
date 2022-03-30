import random
import string
from flask import jsonify, request
from ..model.Cliente import Cliente, ClienteSchema, cliente_schema, clientes_schema
from ..model.Arquivos import db
from datetime import datetime
import configparser
import os

cfg = configparser.ConfigParser()
cfg.read('CONFIG.ini')


DIRETORIO = os.path.abspath(cfg.get("DIRETORIO", "CAMINHO"))

def create_cliente():
    resp = request.get_json()
    nome = resp['nome']
    email = resp['email']
    data_criacao = datetime.strptime(resp['data_criacao'], '%Y-%m-%d').date() 

    stringKey = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
    token_acesso = ''.join(random.choice(stringKey) for i in range(15))

    try:
        cliente = Cliente(nome=nome, email=email, data_criacao=data_criacao, token_acesso=token_acesso)
        db.session.add(cliente)
        db.session.commit()
        try:
            os.mkdir(DIRETORIO+'/'+cliente.token_acesso)
        except OSError as o:
            return jsonify({'msg': 'Não foi possível criar o diretório', 'dados': '', 'error': str(o)})
        return jsonify({'msg': 'Cadastrado com sucesso', 'dados': cliente_schema.dump(cliente), 'error': ''})
    except Exception as e:        
        return jsonify({'msg': 'Não foi possível efetuar o cadastro', 'dados': '', 'error': str(e)})
