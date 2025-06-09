#arquivo para rotas 
from main import app
from flask import render_template, redirect, url_for, request

@app.route('/home') #rota tela inicial
def homepage():
    return render_template("homepage.html")

@app.route('/login') #rota login
def login():
    return render_template("login.html")

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
