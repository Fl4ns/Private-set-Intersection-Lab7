from flask import Flask, request, jsonify
from pathlib import Path
import csv

ruta = Path(__file__).parent / "credenciales.csv"

with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
    reader = csv.DictReader(archivo)
    passwords = {fila["contrasena"] for fila in reader}
app = Flask(__name__)


@app.route("/")
def inicio():
    return "¡Servidor Flask funcionando!"


@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"Hola, {nombre}"




@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data["password"]
    if password in passwords:
        return jsonify({"password_valid": True})
    return jsonify({"password_valid": False})








if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
