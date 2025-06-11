from db import db

class Cliente(db.Model): #tabela cliente do banco de dados
    __tablename__ = 'clientes'
    
    def __init__(self, name_cliente, email, user_cliente, senha_cliente, atividade = True):
        self.name_cliente = name_cliente
        self.email = email
        self.user_cliente = user_cliente
        self.senha_cliente = senha_cliente
        self.atividade = atividade
        
    #campos coluna da tabela
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name_cliente = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = False, nullable = False)
    user_cliente = db.Column(db.String(100), unique = True, nullable = False)
    senha_cliente = db.Column(db.String(100) , nullable = False)
    atividade = db.Column(db.Boolean, nullable = False)
    
class Funcionario(db.Model): #tabela funcionario do banco de dados
    __tablename__ = 'funcionarios'
    
    #inicializador da classe
    def __init__(self, name_funcionario, email, cpf, user_funcionario, senha_funcionario, atividade = True):
        self.name_funcionario = name_funcionario
        self.email = email
        self.cpf = cpf
        self.user_funcionario = user_funcionario
        self.senha_funcionario = senha_funcionario
        self.atividade =  atividade
        
    #campos coluna da tabela
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name_funcionario = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    cpf = db.Column(db.String(100), unique = True, nullable = False)
    user_funcionario = db.Column(db.String(100) , unique = True, nullable = False)
    senha_funcionario = db.Column(db.String(100) , nullable = False) 
    atividade = db.Column(db.Boolean, nullable = False)   
