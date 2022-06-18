from flask import Flask, render_template, redirect, request, flash, session
from app import app, db
from app.models.tables import Usuario, Restaurante, Cardapio
from app.models.seguranca import ControleAcesso


@app.route('/inicial')
def inicial():
    lista_restaurantes = Restaurante.query.all()
    controle_acesso = ControleAcesso.verificar()
    if controle_acesso == False:
        return redirect('/')

    else:
        return render_template('inicial.html', restaurantes=lista_restaurantes)


@app.route('/cardapio')
def cardapio():
    lista_cardapios = Cardapio.query.all()
    controle_acesso = ControleAcesso.verificar()
    if controle_acesso == False:
        return redirect('/')

    else:
        return render_template('pesquisa_cardapio.html', cardapio=lista_cardapios)


