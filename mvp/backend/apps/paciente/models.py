from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.postgresql import JSONB
from apps.core.db import db

#Inserindo toda a classe SQLalchemy(que é uma ?ORL? de automatização de manipulação de banco de dados)
# na variável db para poder instaciar durante a criação e manupulação do banco.


#Criando a classe Paciente e instaciando db.Model e SerializerMixin. 
class Paciente(db.Model, SerializerMixin):
    
    serialize_only = ('id', 'nome', 'cpf','cep', 'rua', 'bairro')
    # id = cria um número identificador para cara paciente e é obrigatório durante a adição de novos pacientes.   
    # nome = Nome do paciente.   
    # cpf = CPF para o cadastro e localização do indivíduo.
    # cep = Indica o CEP da pessoa.


    #Definindo quais seram os métodos da tabela Paciente.    
    id = db.Column("pk_paciente", db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(255), nullable=False)
    rua = db.Column(db.String(255), nullable=True)
    bairro = db.Column(db.String(255), nullable=True)

    #Definindo quais seram as funções dos métodos inseridos em Paciente. 
    def __init__ (self,nome, cpf,cep, bairro, rua):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.bairro = bairro
        self.rua = rua
