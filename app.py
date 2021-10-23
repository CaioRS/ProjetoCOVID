
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/estado')
def estado():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/"
    uf = request.args.get("q")
    if(uf):
        url += uf

    response = requests.get(url)
    dados = response.json()
    return render_template("estado.html", info=dados)


@app.route('/estados')
def estados():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1"
    response = requests.get(url)
    dados = response.json()
    return render_template("estados.html", info=dados)


@app.route('/paises')
def paises():  # put application's code here

    url = "https://covid19-brazil-api.now.sh/api/report/v1/countries"
    response = requests.get(url)
    dados = response.json()
    return render_template("paises.html", info=dados)


if __name__ == '__main__':
    app.run(Debug = True)
