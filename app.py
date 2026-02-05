from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a MongoDB (ajusta el host si tu contenedor tiene otro nombre)
client = MongoClient('mongodb://bayeta_mongo:27017/')
db = client['frases_db']           # Nombre de tu base de datos
coleccion = db['frases']           # Nombre de la colección

# Endpoint para añadir frases
@app.route('/frotar/add', methods=['POST'])
def add_frases():
    data = request.get_json()
    if not data or 'frases' not in data:
        return jsonify({'mensaje': 'No se recibieron frases'}), 400

    frases = [{'texto': frase} for frase in data['frases']]
    coleccion.insert_many(frases)
    return jsonify({'mensaje': f'{len(frases)} frases añadidas'}), 201

# Endpoint para listar todas las frases
@app.route('/frotar', methods=['GET'])
def listar_frases():
    frases = [f['texto'] for f in coleccion.find()]
    return jsonify(frases)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

