from functools import wraps
from flask import request
from ..model.Cliente import Cliente, ClienteSchema, cliente_schema, clientes_schema



def valida_token_acesso(access):
    try:
        client = Cliente.query.filter(Cliente.token_acesso == access).one()
        if not client:
            return False
        return True
    except:
        return False

