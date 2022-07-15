import requests

URL = "http://127.0.0.1:8000/api/Seguridad/signup/"
URLogin = "http://127.0.0.1:8000/api/Seguridad/login/"
PARAMS = {"UserAccess":"admin","PassAccess":"admin"}
r = requests.post(url = URL, json = PARAMS)
data = r.json()
print(data)