import requests as requests

# Variables
BASE = "http://127.0.0.1:5000/"

print("----------------------------------------------------------------------------")
print("RESULT FROM POST")
response = requests.post(BASE + "employees/1", {"name": "Julia Hendricks", "age": 32, "position": "Worker"})
print(response)
print(response.json())


print("----------------------------------------------------------------------------")
print("RESULT FROM GET: ")
response = requests.get(BASE + "employees/1")
print(response.json())

print("----------------------------------------------------------------------------")
print("RESULT FROM PUT: ")
response = requests.put(BASE + "employees/1", {"name": "Julia Carlson", "age": 31, "position": "CEO"})
print(response.json())

print("----------------------------------------------------------------------------")
print("RESULT FROM GET: ")
response = requests.get(BASE + "employees/1")
print(response.json())

print("----------------------------------------------------------------------------")
print("RESULT FROM DELETE")
response = requests.delete(BASE + "employees/1")
print(response)
