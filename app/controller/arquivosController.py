from datetime import datetime
import json
import os
import configparser
from datetime import datetime
from flask import jsonify, send_from_directory, session
from pyparsing import empty
from ..model.Arquivos import Arquivos, ArquivoSchema, arquivo_schemy, arquivos_schemy
from ..model.Cliente import Cliente
from sqlalchemy import desc
from ..model.Arquivos import db


cfg = configparser.ConfigParser()
cfg.read('CONFIG.ini')


DIRETORIO = os.path.abspath(cfg.get("DIRETORIO", "CAMINHO"))


def salva_arquivos(access, file):
    nome_file = file.filename
    nome_arquivo, extensao_aquivo = os.path.splitext(nome_file)

    try:
        arq = Arquivos.query.order_by(desc(Arquivos.id)).first()
        arq_tratado = ''
        if not arq:
            arq_tratado = ''
        else:
            arq_tratado = arq.id

        try:
            client = Cliente.query.filter(Cliente.token_acesso == access).one()
        except:
            return jsonify({'msg': 'Não foi possivel salvar, Cliente nao encontrado'})

        nome_arquivo_banco = datetime.today().strftime(
            '%Y%m%d')+'_'+str(arq_tratado).zfill(4)+extensao_aquivo
        arquivo = Arquivos(data_criacao=datetime.today(),
                           nome_arquivo=nome_arquivo_banco, cliente=client.id)
        db.session.add(arquivo)
        file.save(os.path.join(DIRETORIO+'/'+access, nome_arquivo_banco))

        db.session.commit()
        return jsonify({'msg': 'Salvo com sucesso', 'id_arquivo': arquivo_schemy.dump(arquivo)['id']})
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Nao foi possivel Salvar'})


def lista_arquivos(access):
    arquivos = []
    for nome_arquivo in os.listdir(DIRETORIO+'/'+access):
        endereco_arquivo = os.path.join(DIRETORIO+'/'+access, nome_arquivo)

        if(os.path.isfile(endereco_arquivo)):
            arquivos.append(nome_arquivo)

    return jsonify(arquivos)


def busca_arquivo(access, id):
    try:
        arquivo = Arquivos.query.filter(Arquivos.id == id).one()
        nome_arquivo_dict = arquivo_schemy.dump(arquivo)
        return send_from_directory(DIRETORIO+'/'+access, nome_arquivo_dict['nome_arquivo'], as_attachment=False)
    except Exception as e:
        return jsonify({'msg': 'Nao foi possivel buscar', 'error': str(e)})


def exclui_arquivo(access, id):
    try:
        arquivo = Arquivos.query.filter(Arquivos.id == id).one()
        nome_arquivo_dict = arquivo_schemy.dump(arquivo)
        try:
            os.remove(DIRETORIO+'/'+access+'/'+str(nome_arquivo_dict['nome_arquivo']))
            try:
                db.session.delete(Arquivos.query.get(id))
                db.session.commit()
                return jsonify({'msg': 'Arquivo Excluido com sucesso'})
            except Exception as e:
                return jsonify({'msg': 'Não foi possível excluir o arquivo do banco', 'error': str(e)})
        except OSError as e:
            return jsonify({'msg': 'Nao foi possivel excluir o arquivo', 'error': str(e)})
    except Exception as e:
        return jsonify(str(e))
