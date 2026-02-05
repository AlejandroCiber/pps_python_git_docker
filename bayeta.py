from pymongo import MongoClient
import os
import random

# Conexión a Mongo (usa el nombre del servicio en docker-compose)
MONGO_HOST = os.getenv("MONGO_HOST", "bayeta_mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["bayeta_db"]
collection = db["frases"]

# Función para obtener N frases aleatorias
def frotar(n_frases: int = 1) -> list:
    frases = list(collection.find({}, {"_id": 0}))
    frases_texto = [f["texto"] for f in frases]
    return random.sample(frases_texto, min(n_frases, len(frases_texto)))

# Función para insertar nuevas frases
def add_frases(nuevas_frases: list):
    for frase in nuevas_frases:
        collection.insert_one({"texto": frase})

