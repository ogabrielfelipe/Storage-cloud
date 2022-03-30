
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()


class Arquivos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_criacao = db.Column(db.Date, nullable=False)
    nome_arquivo = db.Column(db.String(25), unique=True, nullable=False)
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    
    def __init__(self, data_criacao, nome_arquivo, cliente):
        self.data_criacao = data_criacao
        self.nome_arquivo = nome_arquivo
        self.cliente = cliente

class ArquivoSchema (ma.Schema):
    class Meta:
        fields = ('id', 'data_criacao', 'nome_arquivo', 'cliente')


arquivo_schemy = ArquivoSchema()
arquivos_schemy = ArquivoSchema(many=True)
