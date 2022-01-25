#Belajar tipe data dictionary

customer = {"Name": "Erwin","Age": 24,"Address":"Semarang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "C"
customer["Name"] = "Budionon"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}: {value}")