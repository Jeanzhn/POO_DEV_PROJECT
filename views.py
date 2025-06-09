#arquivo para rotas 
from main import app
from flask import render_template

@app.route('/') #rota tela inicial
def homepage():
    return render_template("homepage.html")

@app.route('/login') #rota login
def login():
    return render_template("login.html")

@app.route('/password?') #rota esqueci senha
def perdi_senha():
    return render_template('esquecisenha.html')

@app.route('/menu') #rota para
def menu_restaurante():
    return render_template("cliente_acesso.html")

@app.route('/configAdmin') #rota para o painel administrativo
def painel_admin():
    return render_template("page_admin.html")

@app.route('/perfil') #rota para o painel funcionario
def painel_perfil_CLT():
    return render_template("perfil_user.html")
