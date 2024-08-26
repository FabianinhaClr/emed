from flask import Blueprint, render_template
from database.paciente import PACIENTE
paciente_route = Blueprint('paciente', __name__)

#Rotas de usuario:

#usuario/[GET] - Listar Usuários
@usuario_route.route('/')
def listarPaciente():
    return render_template('listarPaciente.html'
    , paciente = PACIENTE)

#usuario/[GET] - inserir usuarios no BD
@usuario_route.route('/', methods=['POST'])
def inserirPaciente():
    pass 

#usuario/new[GET] - renderizar o formulário para criar um novo usuario
@usuario_route.route('/new', methods=['GET'])
def formPaciente():
    return render_template('formPaciente.html')
    

#usuario/<id>[GET] - obter dados do usuario
@usuario_route.route('/<int:usuario_id>', methods=['GET'])
def obterPaciente(usuario_id):
    return render_template('obterPaciente.html')

#usuario/<id>/editar [GET] - editar dados do usuario
@usuario_route.route('/<int:usuario_id>/editar', methods=['GET'])
def editarPaciente(usuario_id):
    return render_template('editarPaciente.html')

#usuario/<id>/update [PUT] - atualizar dados do usuario
@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def updateUsuario(usuario_id):
    pass

#usuario/<id>/delete [DETELE] - deletar dados do usuario
@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletarUsuario(usuario_id):
    pass
