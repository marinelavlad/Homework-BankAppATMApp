import json
import datetime
import random


def card_bancar():
    id_client = input("Introdu id_ul clientului pentru care se doreste emiterea cardului bancar:> ")
    file_clienti = open(
        "./bankpackage/clients.json", 'r')
    clienti_to_dictionar = json.load(file_clienti)
    gasit = 0
    for cheie_id in clienti_to_dictionar:
        if str(id_client) == str(cheie_id):
            gasit = 1
            nume_client = clienti_to_dictionar[id_client]["nume"] + " " + clienti_to_dictionar[id_client]["prenume"]
            print(
                f'Id-ul {id_client} a fost gasit si apartine clientului {nume_client}.')
    if gasit == 0:
        print(f'Id-ul {id_client} nu exista! Incearca din nou.')
    file_clienti.close()

    if gasit == 1:
        file_card = open("./atmpackage/card.json", "r")
        card_to_dict = json.load(file_card)
        file_card.close()

        # generez un nr de card unic
        flag = True
        while flag:
            numar_card = ""
            for i in range(0, 16):
                numar_card += str(random.randint(0, 9))
            unic = 1
            for cheie_card in card_to_dict:
                if cheie_card == numar_card:
                    unic = 0
            if unic == 1:
                flag = False
        cvc = ""
        for i in range(0, 3):
            cvc += str(random.randint(0, 9))
        pin = ""
        for i in range(0, 4):
            pin += str(random.randint(0, 9))

        # emit un card nou pt id-ul clientului ales
        # salvez in fisier card.json unde nr de card generat este cheie
        card_to_dict[numar_card] = {
            "id_client": id_client,
            "titular card": nume_client,
            "data expirare": str(datetime.datetime.now())[5:7] + "/" + str(int(str(datetime.datetime.now())[:4]) + 2),
            "cvc": cvc,
            "pin": pin,
            "moneda": "RON"
        }
        print(f"\nCardul a fost emis cu succes:\nNumar card: {numar_card}\nTitular card: {nume_client}\nData expirare:{str(datetime.datetime.now())[5:7] + '/' + str(int(str(datetime.datetime.now())[:4]) + 2)}\nCVC:{cvc}\nPIN initial:{pin}\n")
        card_to_json = json.dumps(card_to_dict, indent=4)

        file_card = open("./atmpackage/card.json", "w")
        file_card.write(card_to_json)
        file_card.close()