#arquivo para rotas 
from main import app
from flask import render_template, redirect, url_for, request, jsonify, session
from models.pessoas import db, Cliente
from models.crud import CRUD
from models.pessoas import Funcionario
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/') #rota tela inicial
def homepage():
    return render_template("homepage.html")

@app.route('/login', methods = ['POST' , 'GET']) #rota login
def login():
    if request.method == 'POST':
        login_cliente = request.form['login']
        senha_cliente = request.form['senha_cliente']
        
        user_exist = Cliente.query.filter_by(
            user_cliente = login_cliente, 
            senha_cliente = senha_cliente
        ).first() 
        if user_exist:
            print('Login com sucesso')
            return render_template("cliente_acesso.html")
        else:
            return render_template("login.html", error = "Usuário ou senha incorretos")
    return render_template("login.html")


@app.route('/register', methods = ['POST', 'GET']) #rota para se registrar, criando seu proprio usuario
def register_cliente():
    if request.method == 'POST':
        name_cliente = request.form['nome_cliente']
        user_cliente = request.form['user_cliente']
        email = request.form['email']
        senha_cliente = request.form['senha_cliente']
        
        novo_user= CRUD()
        novo_user.create_user(
            name_cliente = name_cliente, 
            user_cliente = user_cliente, 
            email = email, 
            senha_cliente = senha_cliente
        )
        return redirect(url_for('menu_restaurante')) 
    return render_template('register.html')

@app.route('/password?') #rota esqueci senha
def perdi_senha():
    return render_template('esquecisenha.html')

@app.route('/menu') #rota para tela cliente pedido
def menu_restaurante():
    return render_template("cliente_acesso.html")

@app.route('/configAdmin') #rota para o painel administrativo
def painel_admin():
    return render_template("page_admin.html")

@app.route('/perfil_clt/<nome_funcionario>') #rota para o painel funcionario com uma variavel nome funcionario sendo repassada
def painel_perfil_CLT(nome_funcionario):
    return render_template("perfil_funcionario.html", nome_funcionario=nome_funcionario)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/adicionar_funcionario', methods=['GET', 'POST'])
def adicionar_funcionario():
    if not session.get('autorizado'):
        return redirect(url_for('painel_perfil_CLT', nome_funcionario=session.get('nome_funcionario')))

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        autorizado = 'autorizado' in request.form

        novo = Funcionario(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha),
            autorizado=autorizado
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('painel_perfil_CLT', nome_funcionario=session.get('nome_funcionario')))
    
    return render_template('adicionar_funcionario.html')

@app.route('/login_funcionario', methods = ['GET', 'POST'])
def login_funcionario():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        funcionario = Funcionario.query.filter_by(email=email).first()
        if funcionario and check_password_hash(funcionario.senha, senha):
            session['nome_funcionario'] = funcionario.nome
            session['funcionario_id'] = funcionario.id
            session['autorizado'] = funcionario.autorizado
            return redirect(url_for('painel_perfil_CLT', nome_funcionario=funcionario.nome))
        else:
            return render_template('login_funcionario.html', error='Credenciais inválidas')
    return render_template('login_funcionario.html')

@app.route('/meu_perfil_funcionario')
def meu_perfil_funcionario():
    funcionario_id = session.get('funcionario_id')
    funcionario = Funcionario.query.get(funcionario_id)
    return render_template("meu_perfil.html", funcionario=funcionario)

@app.route("/clientes") #só pra testar uma teoria
def listar_clientes():
    clientes = Cliente.query.all()
    return {c.id: c.name for c in clientes}
