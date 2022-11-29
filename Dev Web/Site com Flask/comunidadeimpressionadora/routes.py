#AQUI É A PARTE ONDE CRIA TODAS AS FUNÇÕES DE PÁGINAS

from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user

lista_usuarios = ['Lira','João']

@app.route("/")  #Caminho da nossa página
def home():
    return render_template('home.html') #Retorna e renderiza a página home que fica dentro da pasta templates

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios) #Coloca a lista de usuarios como parâmetro aqui para poder chamar ela na página usuarios.html

@app.route("/login", methods=['GET','POST']) #Toda página que tiver formulário tem que passar esse methods get e post.
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_entrar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de login
        #encontra o usuario
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        #Se o usuario existe e a senha do banco de dados é a mesma que ele preencheu no formulário então funciona o login
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            #Faz o login efetivamente
            login_user(usuario, remember=form_login.lembrar_dados.data)
            #Exibe mensagem de sucesso
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            #Redireciona para tal página
            return redirect(url_for('home'))
        else:
            #Exibe mensagem de erro
            flash(f'Falha no Login. E-mail ou Senha incorretos', 'alert-danger')
        
    
    return render_template('login.html', form_login = form_login)

@app.route("/criarconta", methods=['GET','POST'])#Toda página que tiver formulário tem que passar esse methods get e post.
def criar_conta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit() and 'botao_criar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de criar conta
        #Transforma a senha em criptografia
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        #Estamos criando um usuário no banco de dados
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        #Estamos adicionando o usuário na sessão do banco de dados
        database.session.add(usuario)
        #Estamos dando um commit
        database.session.commit()
        #Exibir mensagem
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        #Redireciona para tal página
        return redirect(url_for('home'))

    return render_template('criarconta.html', form_criarconta = form_criarconta)

#Faz o logout e redireciona pra home
@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso!!', 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/post/criar')
def criar_post():
    return render_template('criarpost.html')