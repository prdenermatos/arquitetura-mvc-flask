
from flask import Flask, render_template, redirect, request, flash
from app import app, db
from app.models.tables import Usuario
from app.models.seguranca import Criptografia



@app.route('/cadastro')
def cadastro():
    return render_template('cadastro_usuario.html')

@app.route('/cadastramento_usuario', methods=["POST"])
def cadastramento():

    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    senha_cripto = Criptografia(senha)
    senha_segura = senha_cripto.criptografar()

    novo_usuario = Usuario(nome, email, senha_segura)
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Cadastro realizado com sucesso! ')

    
    return redirect('/')
