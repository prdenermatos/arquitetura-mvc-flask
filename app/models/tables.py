from flask_sqlalchemy import SQLAlchemy
from app import db


class Paciente(db.Model):
    __tablename__ = "cad_pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    cpf = db.Column(db.String(10))
    endereco = db.Column(db.String(30))
    relato = db.Column(db.String(100))

    def __init__(self, nome, cpf, endereco, relato):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.relato = relato

    def __repr__(self):
        return '<Paciente %r>' % self.nome    


