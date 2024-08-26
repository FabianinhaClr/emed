from flask import Blueprint, render_template
from database.medico import MEDICO
medico_route = Blueprint('medico', __name__)

#Rotas de usuario:

#usuario/[GET] - Listar Usuários
@usuario_route.route('/')
def listarUsuario():
    return render_template('listarUsuario.html'
    , usuario = USUARIO)

#usuario/[GET] - inserir usuarios no BD
@usuario_route.route('/', methods=['POST'])
def inserirUsuario():
    pass 

#usuario/new[GET] - renderizar o formulário para criar um novo usuario
@usuario_route.route('/new', methods=['GET'])
def formUsuario():
    return render_template('formUsuario.html')
    

#usuario/<id>[GET] - obter dados do usuario
@usuario_route.route('/<int:usuario_id>', methods=['GET'])
def obterUsuario(usuario_id):
    return render_template('obterUsuario.html')

#usuario/<id>/editar [GET] - editar dados do usuario
@usuario_route.route('/<int:usuario_id>/editar', methods=['GET'])
def editarUsuario(usuario_id):
    return render_template('editarUsuario.html')

#usuario/<id>/update [PUT] - atualizar dados do usuario
@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def updateUsuario(usuario_id):
    pass

#usuario/<id>/delete [DETELE] - deletar dados do usuario
@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletarUsuario(usuario_id):
    pass
