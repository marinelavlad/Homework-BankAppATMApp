import json
import datetime


def interogare_sold(nr_card):
    file_card = open("./atmpackage/card.json", "r")
    card_to_dict = json.load(file_card)
    file_card.close()

    id_client = card_to_dict[nr_card]["id_client"]

    file_banca = open("./bankpackage/banca.json", "r")
    banca_to_dict = json.load(file_banca)
    file_banca.close()

    print(f"Sold disponibil: {banca_to_dict[id_client]['balanta']} lei")



def retragere_numerar(nr_card):
    file_card = open("./atmpackage/card.json", "r")
    card_to_dict = json.load(file_card)
    file_card.close()

    id_client = card_to_dict[nr_card]["id_client"]

    # Extragere numerar de la ATM
    file_banca = open("./bankpackage/banca.json", "r")
    banca_to_dictionar = json.load(file_banca)
    file_banca.close()
    print(f"Sold disponibil: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
    suma = float(input("Introdu suma:> "))
    if suma > 0:
        file_banca = open("./bankpackage/banca.json", "r")
        banca_to_dictionar = json.load(file_banca)
        file_banca.close()
        noul_debit = float(banca_to_dictionar[id_client]['balanta']) - suma
        if noul_debit >= 0:
            file_banca = open("./bankpackage/banca.json", "r")
            banca_to_dictionar = json.load(file_banca)
            banca_to_dictionar[id_client]['balanta'] = noul_debit
            print("Retragere numerar efectuata cu succes!\nNu uita sa iei banii din bancomat!")
            file_banca.close()

            banca_to_json = json.dumps(banca_to_dictionar, indent=4)

            file_banca = open("./bankpackage/banca.json", 'w')
            file_banca.write(banca_to_json)
            file_banca.close()

            file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
            tranzactii_to_dictionar = json.load(file_tranzactii)
            tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
                "Detalii Tranzactie": ["Retragere numerar de la ATM"],
                "Debit": suma,
                "Credit": float(0),
                "Balanta": noul_debit
            }
            file_tranzactii.close()

            tranzactii_to_json = json.dumps(tranzactii_to_dictionar, indent=4)

            file_tranzactii = open('./bankpackage/tranzactii.json', 'w')
            file_tranzactii.write(tranzactii_to_json)
            file_tranzactii.close()
        else:
            print("Tranzactie esuata! Sold insuficient!")
            print(f"Soldul disponibil este: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
    else:
        print("Suma introdusa este < = 0. Incearca din nou, introducand un numar pozitiv!")


def depunere_numerar(nr_card):
    file_card = open("./atmpackage/card.json", "r")
    card_to_dict = json.load(file_card)
    file_card.close()

    id_client = card_to_dict[nr_card]["id_client"]

    # Depunere numerar la ATM
    suma = float(input("Introdu suma:> "))
    if suma > 0:
        file_banca = open("./bankpackage/banca.json", "r")
        banca_to_dictionar = json.load(file_banca)
        file_banca.close()

        noul_credit = float(banca_to_dictionar[id_client]["balanta"]) + suma
        banca_to_dictionar[id_client]["balanta"] = noul_credit
        print("Depunere numerar realizata cu succes! Va multumim!")

        banca_to_json = json.dumps(banca_to_dictionar, indent=4)

        file_banca = open("./bankpackage/banca.json", "w")
        file_banca.write(banca_to_json)
        file_banca.close()

        file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
        tranzactii_to_dictionar = json.load(file_tranzactii)
        tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
            "Detalii Tranzactie": ["Depunere numerar la ATM"],
            "Debit": float(0),
            "Credit": suma,
            "Balanta": noul_credit
        }
        file_tranzactii.close()

        tranzactii_to_json = json.dumps(tranzactii_to_dictionar, indent=4)

        file_tranzactii = open('./bankpackage/tranzactii.json', 'w')
        file_tranzactii.write(tranzactii_to_json)
        file_tranzactii.close()
    else:
        print("Suma introdusa este < = 0. Incearca din nou!")