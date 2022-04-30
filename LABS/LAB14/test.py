import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "employee/1", {"name": "Til", "age": "40"})
print(response)
print(response.json())
