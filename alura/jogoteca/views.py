from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Usuarios

@app.route("/")
def index():   
     lista = Jogos.query.order_by(Jogos.id)  
     return render_template('lista.html', titulo = 'Jogos', jogos=lista)


@app.route("/novo")
def novo():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
          return redirect(url_for('login', proxima=url_for('novo')))
     return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST' ,])
def criar():

     nome = request.form['nome']
     categoria = request.form['categoria']
     console = request.form['console']
     jogo = Jogos.query.filter_by(nome=nome).first()

     if jogo:
         flash('Jogo Existente!')
         return redirect(url_for('index'))
     novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
     db.session.add(novo_jogo)
     db.session.commit()

     arquivo = request.files['arquivo']
     arquivo.save(f'uploads/{arquivo.filename}')
     

     return redirect(url_for('index'))

@app.route("/editar/<int:id>")
def editar(id):
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
          return redirect(url_for('login', proxima=url_for('editar', id=id)))
     jogo = Jogos.query.filter_by(id=id).first()
     return render_template('editar.html', titulo='Editando Jogo', jogo=jogo)
     

@app.route('/atualizar', methods=['POST' ,])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('index'))
    

@app.route('/login')
def login():
     proxima = request.args.get('proxima')
     return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname = request.form['usuario']).first()
    if usuario:     
       if request.form['senha'] == usuario.senha:
          session['usuario_logado'] = usuario.nickname
          flash(usuario.nickname +  ' logado com sucesso!')
          proxima_pagina = request.form['proxima']
          return redirect(proxima_pagina)
    else:
      flash('Usuário nao Logado')
      return redirect(url_for('login'))  
    
@app.route('/deletar/<int:id>')    
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
          return redirect(url_for('login'))
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo Deletado com Sucesso!')

    return redirect(url_for('index'))

    
     
@app.route('/logout')
def logoult():
     session['usuario_logado'] = None
     flash('Logout efetuado com sucesso!')
     return redirect(url_for('index'))