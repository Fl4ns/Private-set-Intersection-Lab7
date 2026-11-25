import requests

password = input("Ingrese su contraseña: ")

response = requests.post(
    "http://127.0.0.1:5000/check",
    json={"password": password}
)

print(response.json())