from flask import Flask, render_template, redirect, request
from app import app, db
from app.models.tables import Paciente

ids= dict()

@app.route('/delecao/<int:id>')
def delecao(id):
    paciente = Paciente.query.filter_by(id=id)
    ids['n'] = id
    return render_template("confirma_delecao.html", paciente=paciente)

@app.route('/apagar')
def apagar():
    ID = ids['n']
    paciente = Paciente.query.filter_by(id=ID).first()

    db.session.delete(paciente)
    db.session.commit()
    return redirect('/consulta')