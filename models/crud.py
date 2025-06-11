from db import db
from models.pessoas import Cliente

class CRUD():
    def create_user(self, name_cliente , email, user_cliente, senha_cliente):
        try:
            name_user_exist = Cliente.query.filter_by(user_cliente = user_cliente).first()
            
            if name_user_exist:
                print('Este nome de usuario não está disponivel, tente outro')
                return
            
            new_user = Cliente(name_cliente = name_cliente, email = email, user_cliente = user_cliente, senha_cliente = senha_cliente)
            db.session.add(new_user)
            db.session.commit()
            db.session.close()
            
            print('Usuario cadastrado sucesso')
        except TypeError as e:
             print(f"Erro ao criar usuário: {e}")
             
    @staticmethod         
    def update_user(id ,campo_alvo, new_valor):
        try:
            id_user = Cliente.query.get(id)
            if not id_user:
                print("Usuario não encontrado")
                return False
            
            if hasattr(id_user, campo_alvo): #verifica se para o usuario existe o campo alvo
                
                CAMPOS_PERMITIDOS = {'name_cliente', 'email', 'user_cliente'} 
                
                if campo_alvo not in CAMPOS_PERMITIDOS:
                    print(f"Campo '{campo_alvo}' não é editável.")
                    return False
            
                setattr(id_user, campo_alvo, new_valor) #set um novo valor com base no usuario identificado com id, no campo_alvo escolhido
                db.session.commit()
                print(f'Campo {campo_alvo} alterado com sucesso para {new_valor}')
                return True
            else:
                print(f'Campo {campo_alvo} não existe para modelo cliente')
                return False
            
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False
            