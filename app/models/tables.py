from flask_sqlalchemy import SQLAlchemy
from app import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    email = db.Column(db.String(30))
    senha = db.Column(db.String(30))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def __repr__(self):
        return '<Usuario %r>' % self.nome    

class Restaurante(db.Model):
    __tablename__ = "restaurantes"

    id = db.Column(db.Integer, primary_key=True)
    restaurante = db.Column(db.String(20))
    rua_numero = db.Column(db.String(30))
    bairro = db.Column(db.String(30))
    categoria = db.Column(db.String(30))
    diferencial1 = db.Column(db.String(30))
    diferencial2 = db.Column(db.String(30))
    diferencial3 = db.Column(db.String(30))
    descricao_foto = db.Column(db.String(10))

    def __init__(self, restaurante, rua_numero, bairro, categoria, diferencial1, diferencial2, diferencial3, descricao_foto):
        self.restaurante = restaurante
        self.rua_numero = rua_numero
        self.bairro = bairro
        self.categoria = categoria
        self.diferencial1 = diferencial1
        self.diferencial2 = diferencial2
        self.diferencial3 = diferencial3
        self.descricao_foto = descricao_foto


    def __repr__(self):
        return '<Restaurante %r>' % self.restaurante 


class Cardapio(db.Model):
    __tablename__ = "cardapios"

    id = db.Column(db.Integer, primary_key=True)
    prato = db.Column(db.String(20))
    restaurante = db.Column(db.String(30))
    descricao = db.Column(db.String(30))
    preco = db.Column(db.Float(30))
    descricao_foto = db.Column(db.String(30))


    def __init__(self, prato, restaurante, descricao, preco, descricao_foto):
        self.prato = prato
        self.restaurante = restaurante
        self.descricao = descricao
        self.preco = preco
        self.descricao_foto = descricao_foto


    def __repr__(self):
        return '<Cardapio %r>' % self.prato 
