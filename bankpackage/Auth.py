# functie auth

import json
dictionar_auth = {
    "1": {"mari": "123"},
    "2": {"bogdan": "456"},
    "3": {"vlad": "789"}
}

auth_to_json = json.dumps(dictionar_auth, indent=4) #pune 4 spatii ca sa arate ca un tab

file = open("./bankpackage/auth.json", "w")
file.write(auth_to_json)
file.close()


def login(username, password):
    file_auth = open('./bankpackage/auth.json', 'r')
    auth_to_dictionar = json.load(file_auth)
    file_auth.close()

    gasire_user = 0

    for cheie_user in auth_to_dictionar.values():
        for cheie_nume in cheie_user:
            if cheie_nume == username:
                gasire_user = 1
                if cheie_user[cheie_nume] == password:
                    print('Login successful')
                    return True
                else:
                    return 'password gresit'

    if gasire_user == 0:
        return 'username gresit'