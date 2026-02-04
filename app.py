from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, mundo"

@app.route('/frotar/<int:n_frases>')
def frotar_endpoint(n_frases):
    # Por ahora devuelve la misma frase repetida N veces
    return jsonify(frotar(n_frases))

if __name__ == '__main__':
    app.run(debug=True)

