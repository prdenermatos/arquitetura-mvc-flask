from flask import flash, redirect, session
from hashlib import md5

class Criptografia():
    '''Classe responsável pela criptografia no cadastro de senhas
    '''
    def __init__(self, senha):
        self.hashed = senha.encode("utf8")

    def criptografar(self): 
        senha_cripto = md5(self.hashed).hexdigest()
        return senha_cripto
    

class Autenticacao():
    ''' Classe responsável pela verificação de cadastro (usando descriptografia) 
    '''
    def __init__(self, email, senha):
        self.email = email
        cripto_senha = Criptografia(senha)
        self.senha = cripto_senha.criptografar()
    
    def verificar(self, dados_db):
        registros_email = list()
        registros_senhas = list()
        for dado in dados_db:
            registros_email.append(dado.email)
            registros_senhas.append(dado.senha)

        if self.email in registros_email:
            if self.senha in registros_senhas:
                return True
        else:
            return False


class ControleAcesso:
    def verificar():        
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            flash('Para acessar o sistema é necessário fazer o login!')
            return False
        else:
            return True




