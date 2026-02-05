from flask import Flask, request, jsonify
from bayeta import frotar, add_frases  # Importamos funciones de bayeta.py

app = Flask(__name__)

# Endpoint GET: devuelve todas las frases aleatorias (1 por defecto)
@app.route('/frotar', methods=['GET'])
def listar_frases():
    return jsonify(frotar(1))

# Endpoint GET dinámico: devuelve n frases aleatorias
@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases_endpoint(n_frases):
    return jsonify(frotar(n_frases))

# Endpoint POST: añade nuevas frases
@app.route('/frotar/add', methods=['POST'])
def añadir_frases():
    data = request.get_json()
    if not data or 'frases' not in data:
        return jsonify({'mensaje': 'No se recibieron frases'}), 400
    add_frases(data['frases'])
    return jsonify({'mensaje': f'{len(data["frases"])} frases añadidas'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

