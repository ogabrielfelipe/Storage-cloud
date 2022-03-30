import os
from flask import Blueprint, jsonify, request, send_from_directory
from datetime import datetime
from ..controller.helper import valida_token_acesso

from ..controller.arquivosController import salva_arquivos, lista_arquivos, busca_arquivo, exclui_arquivo



api_arq = Blueprint('api_arq', __name__)


@api_arq.route('/<string:access>/arquivos/lista', methods=['GET'])
def lista_route_arquivos(access):
    result = valida_token_acesso(access=access)
    if result:
        return lista_arquivos(access)
    else:
        return jsonify({'msg': 'Cliente não e valido'})


@api_arq.route('/<string:access>/arquivos/<int:id>', methods=['GET'])
def busca_route_arquivo(access, id):
    result = valida_token_acesso(access=access)
    if result:
        return busca_arquivo(access, id)
    else:
        return jsonify({'msg': 'Cliente não e valido'})


@api_arq.route('/<string:access>/arquivos/envia', methods=['POST'])
def envia_route_arquivos(access):
    result = valida_token_acesso(access=access)
    if result:
        file = request.files.get("arquivo")
        return salva_arquivos(access, file)
    else:
        return jsonify({'msg': 'Cliente não e valido'})


@api_arq.route('/<string:access>/arquivos/excluir/<int:codigo>', methods=['GET'])
def exclui_route_arquivo(access, codigo):
    result = valida_token_acesso(access=access)
    if result:
        return exclui_arquivo(access, codigo)
    else:
        return jsonify({'msg': 'Cliente não e valido'})
