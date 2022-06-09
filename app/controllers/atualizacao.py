from flask import Flask, render_template, redirect, request
from app import app, db
from app.models.tables import Paciente

@app.route('/atualizacao/<int:id>')
def atualizacao(id):
    ID = id 
    paciente = Paciente.query.filter_by(id=ID).first()
    return render_template('atualizacao.html', paciente=paciente)

@app.route('/edicao', methods=["POST"])
def edicao():
    # Exclusão registro antigo
    id = request.form['id']
    paciente_exclusao = Paciente.query.filter_by(id=id).first()
    db.session.delete(paciente_exclusao)

    #inclusão atualizado

    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    relato = request.form['relato']
    paciente_atualizado = Paciente(nome, cpf, endereco, relato)

    db.session.add(paciente_atualizado)
    db.session.commit()

    return redirect('/consulta')
  
    





    

    return redirect('/consulta')