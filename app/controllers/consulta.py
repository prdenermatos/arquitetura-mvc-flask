from flask import Flask, render_template, redirect, request
from app import app
from app.models.tables import Restaurante, Cardapio


# consultas dinâmicas


@app.route('/consulta_restaurante', methods=["POST"])
def consulta_restaurante():
    consulta = '%'+request.form.get('consulta')+'%'
    campo = request.form.get('campo')

    if campo == 'restaurante':
        lista_restaurante = Restaurante.query.filter(Restaurante.restaurante.like(consulta)).all()
    elif campo == 'bairro':
        lista_restaurante = Restaurante.query.filter(Restaurante.bairro.like(consulta)).all()
    elif campo == 'categoria':
        lista_restaurante = Restaurante.query.filter(Restaurante.categoria.like(consulta)).all()
    else:
        lista_restaurante = Restaurante.query.all()
    return render_template('/inicial.html', restaurantes=lista_restaurante)



@app.route('/consulta_cardapio', methods=["POST"])
def consulta_cardapio():
    consulta = '%'+str(request.form.get('consulta_cardapio'))+'%'
    campo = request.form.get('campo_cardapio')
    if campo == 'prato':
        lista_cardapios = Cardapio.query.filter(Cardapio.prato.like(consulta)).all()
    elif campo == 'restaurante':
        lista_cardapios = Cardapio.query.filter(Cardapio.restaurante.like(consulta)).all()
    elif campo == 'preco':
        lista_cardapios = Cardapio.query.filter(Cardapio.preco.like(consulta)).all()
    else:
        lista_cardapios = Cardapio.query.all()
    return render_template('/inicial.html', restaurantes=lista_cardapios)
