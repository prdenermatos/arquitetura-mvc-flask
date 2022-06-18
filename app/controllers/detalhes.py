from flask import Flask, render_template, redirect, request
from app import app
from app.models.tables import Restaurante, Cardapio
from app.models.seguranca import ControleAcesso



@app.route('/detalhes/<int:id>')
def detalhes(id):
    lista_restaurantes = Restaurante.query.filter_by(id=id).first()
    lista_cardapios = Cardapio.query.filter(Cardapio.restaurante.like(lista_restaurantes.restaurante)).all()
    controle_acesso = ControleAcesso.verificar()
    if controle_acesso == False:
        return redirect('/')
    else:
        return render_template('restaurante_detalhes.html', cardapio=lista_cardapios, restaurante=lista_restaurantes)
    
@app.route('/processar_detalhes')
def processar_detalhes():
    return redirect('/detalhes')