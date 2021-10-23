
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def inicio():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/"
    if(request.args.get("name")):
        url = "https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/" + request.args.get("name")
    response = requests.get(url)
    dados = response.json()
    return render_template("Inicio.html",info=dados)


@app.route('/estados')
def estados():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1"
    response = requests.get(url)
    dados = response.json()
    return render_template("estados.html",info=dados)


@app.route('/paises')
def paises():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1/countries"
    response = requests.get(url)
    dados = response.json()
    return render_template("paises.html",info=dados)


if __name__ == '__main__':
    app.run(Debug = True)
