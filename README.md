# Bayeta Flask + MongoDB

Pequeña aplicación en Flask que devuelve frases aleatorias y permite añadir nuevas frases, usando MongoDB como almacenamiento persistente.

## Funcionalidad

- Obtener frases aleatorias desde MongoDB.
- Añadir frases nuevas a la base de datos.
- Persistencia de datos mediante volúmenes de Docker.

---

## Tecnologías usadas

- Python 3.11
- Flask
- MongoDB 7
- Docker y Docker Compose

---

## Levantar la aplicación

1. Clonar el repositorio y entrar en la carpeta del proyecto:

```bash
git clone https://github.com/AlejandroCiber/pps_python_git_docker.git
cd pps_python_git_docker
```
## Levantar los contenedores con Docker Compose:

docker compose up --build

---

## Contenedores:

bayetamongo → MongoDB en el puerto 27017 (volumen persistente mongo_data)

bayeta_flask → Flask en el puerto 5000

Variables de entorno usadas:

MONGOHOST=bayeta_mongo
MONGO_PORT=27017

---

## Ejemplo JSON para POST /frotar/add

{
  "frases": ["Persistente 1", "Persistente 2"]
}

---

## Ejemplos con curl

# Obtener una frase aleatoria
curl http://127.0.0.1:5000/frotar

# Obtener 3 frases aleatorias
curl http://127.0.0.1:5000/frotar/3

# Añadir frases nuevas
curl -X POST http://127.0.0.1:5000/frotar/add \
-H "Content-Type: application/json" \
-d '{"frases": ["Persistente 1", "Persistente 2"]}'

---

## Persistencia de datos

Las frases se almacenan en MongoDB y persisten aunque los contenedores se detengan, gracias al volumen mongo_data definido en Docker Compose.

---
