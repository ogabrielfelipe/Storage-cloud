from flask import Blueprint
from ..controller.clienteController import create_cliente

client = Blueprint('client', __name__)


@client.route('/Cliente/Cadastrar', methods=['POST'])
def create_route_cliente():
    return create_cliente()