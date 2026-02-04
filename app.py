from flask import Flask, jsonify
from bayeta import frotar  # Importamos la función aleatoria

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola, mundo"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

if __name__ == '__main__':
    app.run(debug=True)

