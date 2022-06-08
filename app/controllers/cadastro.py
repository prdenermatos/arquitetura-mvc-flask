
from flask import Flask, render_template, redirect, request
from app import app, db
from app.models.tables import Paciente


@app.route('/')
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastramento', methods=["POST"])
def cadastramento():
    nome_paciente = request.form['nome']
    cpf_paciente = request.form['cpf']
    endereco_paciente =request.form['endereco']
    relato = request.form['relato']
    novo_paciente = Paciente(nome_paciente, cpf_paciente, endereco_paciente, relato)
    db.session.add(novo_paciente)
    db.session.commit()
    
    return redirect('/cadastro')
