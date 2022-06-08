from flask import Flask, render_template, redirect, request
from app import app, db
from app.models.tables import Paciente


@app.route('/consulta')
def consulta():
    cadastros = Paciente.query.all()

    return render_template('consulta.html', pacientes=cadastros)

@app.route("/buscar_paciente", methods = ["POST"])
def buscar_paciente():
    CPF = str(request.form['consulta_cpf']).strip()
    busca = Paciente.query.filter_by(cpf=CPF)
    if busca:
        return render_template('busca_cpf.html', busca = busca)
    else:
        return redirect('/consulta')

    

