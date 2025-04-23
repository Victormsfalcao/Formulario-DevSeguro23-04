from flask import request, render_template
from app import app
from app.autorizacao import verificar_acesso

import re

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if len(nome) < 3:
            return "Nome muito curto"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "E-mail inválido"
        if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", senha):
            return "Senha inválida"

        usuario = {"nome": nome, "papel": "usuario", "idade": 22}
        recurso = {"recurso": "cadastro"}

        if not verificar_acesso(usuario, recurso):
            return "Acesso negado!"

        return "Cadastro realizado com sucesso!"
    return render_template("index.html")
