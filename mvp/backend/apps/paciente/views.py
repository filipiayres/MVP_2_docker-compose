from flask import Blueprint, jsonify, request
from apps.paciente.controllers import (
    create_paciente, 
    get_all_pacientes, 
    get_paciente_by_id, 
    update_paciente, 
    delete_paciente
)

# A views faz a chamada de Blueprint que faz parte do pacote flask e gerencia as rodas
# de GET, POST, PUT, PATCH e DELETE.
views = Blueprint('paciente_views', __name__)

#Faz a busca de todos os pacientes no banco de dados Paciente.
@views.route('/pacientes', methods=['GET'])
def get_pacientes():
    pacientes = get_all_pacientes()
    return jsonify([paciente.to_dict() for paciente in pacientes]), 200

#Faz a busca do paciente pelo seu ID.
@views.route('/pacientes/<int:id>', methods=['GET'])
def get_paciente(id):
    paciente = get_paciente_by_id(id)
    if not paciente:
        return jsonify({'message': 'Paciente not found'}), 404
    return jsonify(paciente.to_dict()), 200
    

#Adiciona novo paciente a base de dados e retorna 201.
@views.route('/pacientes', methods=['POST'])
def add_paciente():
    data = request.get_json()
    paciente = create_paciente(data)

    if not paciente:
        return jsonify({'message': 'Erro ao adicionar paciente'}), 404

    return jsonify(paciente.to_dict()), 201
    

#Substitui informações de paciente a partir do deu ID.
@views.route('/pacientes/<int:id>', methods=['PUT'])
def update_paciente_route(id):
    data = request.get_json()
    paciente = update_paciente(id, data)
    if not paciente:
        return jsonify({'message': 'paciente not found'}), 404
    return jsonify(paciente.to_dict()), 200


#Deletando paciente da base de dados ID.
@views.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente_route(id):
    paciente = delete_paciente(id)
    if not paciente:
        return jsonify({'message': 'Paciente not found'}), 404
    return jsonify({'message': f'Paciente {paciente.nome} removido com sucesso'}), 201
    


