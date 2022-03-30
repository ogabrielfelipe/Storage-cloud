from enum import unique
from .Arquivos import db, ma


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    token_acesso = db.Column(db.String(128), unique=True,nullable=False)
    data_criacao = db.Column(db.Date, nullable=False)
    arquivos = db.relationship("Arquivos")

    def __init__(self, nome, email, token_acesso, data_criacao):
        self.nome = nome
        self.email = email
        self.token_acesso = token_acesso
        self.data_criacao = data_criacao

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'email', 'token_acesso', 'data_criacao', 'arquivos')


cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)
