from apps.paciente.models import Paciente
from apps.core.db import db

#Criando um novo paciente dentro do banco de dados de Paciente.
def create_paciente(paciente):

    new_paciente = Paciente(
        nome=paciente['nome'],
        cpf=paciente['cpf'], 
        cep=paciente['cep'],
        rua=paciente['rua'], 
        bairro=paciente['bairro'],
    )
    db.session.add(new_paciente)
    db.session.commit()
    return new_paciente

#Para listar todos os pacientes e 
# suas informações presentes no banco de dados.
def get_all_pacientes():
    return Paciente.query.all()

#para buscar um paciente através do seu ID.
def get_paciente_by_id(id):
    return Paciente.query.get(id)

#Upando (atualizar) informações ao paciente através do ID.
def update_paciente(id, data):
    paciente = Paciente.query.get(id)
    if paciente:
        paciente.nome = data['nome']
        paciente.cpf = data['cpf']
        paciente.cep = data['cep']
        paciente.bairro = data['bairro']
        paciente.rua = data['rua']
        db.session.commit()
        return paciente
    return None

#Deletando paciente através do ID.
def delete_paciente(id):
    paciente = Paciente.query.get(id)
    if paciente:
        db.session.delete(paciente)
        db.session.commit()
        return paciente
    return None
