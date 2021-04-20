import json

file_clienti = open("./atmpackage/card.json", "r")
clienti_to_dictionar = json.load(file_clienti)

print(clienti_to_dictionar)