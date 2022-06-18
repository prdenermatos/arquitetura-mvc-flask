from flask import Flask, render_template, redirect, request, flash, session
from app import app, db
from app.models.tables import Usuario
from app.models.seguranca import Autenticacao



@app.route('/')
def login():
    return render_template("login.html")

@app.route('/autenticar', methods=["POST"])
def autenticar():
    usuario = request.form['email']
    senha = request.form['senha']
    dados = Usuario.query.all() 
    verificacao = Autenticacao(usuario, senha)
    resposta_verificacao = verificacao.verificar(dados)

    if resposta_verificacao == True:
        session['usuario_logado'] = usuario
        flash("Autenticação realizada")
        return redirect('/inicial')
    else:
        flash("Usuário não encontrado")
        return redirect('/')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect('/') 
    