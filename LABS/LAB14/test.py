import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "employees/1", {"name": "Til", "age": 40})
print(response)
print(response.json())

input()
response = requests.post(BASE + "employees/1", {"name": "Til", "age": 40})
print(response)
print(response.json())

input()
response = requests.get(BASE + "employees/2")
print(response)
print(response.json())

input()
response = requests.get(BASE + "employees/1")
print(response)
print(response.json())

input()
response = requests.delete(BASE + "employees/1")
print(response)
