from flask import Flask, render_template, redirect, request, flash
import json


app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def homepage():
    return render_template('login.html')


@app.route("/Login", methods=['POST'])
def Login():


    return render_template("login1.html")

@app.route("/Home", methods=['POST'])
def home():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'adm' and senha == 'adm':

        return render_template("home.html")
    else:
        return redirect("/Login")


if __name__ == "__main__":
    app.run(debug=True)
    