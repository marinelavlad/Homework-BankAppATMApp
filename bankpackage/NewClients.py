import json
import datetime


def new_client():
    file_clients = open("./bankpackage/clients.json", "r")
    clients_to_dictionar = json.load(file_clients)
    new_id = str(len(clients_to_dictionar) + 1)
    file_clients.close()

    new_nume = input("Numele:> ").title()
    new_prenume = input("Prenume:> ").title()
    new_telefon = input("Telefon:> ")
    new_oras = input("Oras:> ").title()

    # adaug clientul in clients.json
    clients_to_dictionar[f"{new_id}"] = {
        "nume": new_nume,
        "prenume": new_prenume,
        "telefon": new_telefon,
        "oras": new_oras
    }

    clients_to_jason = json.dumps(clients_to_dictionar, indent=4)

    file_clients = open('./bankpackage/clients.json', 'w')
    file_clients.write(clients_to_jason)
    file_clients.close()

    print(f"Contul clientului {new_nume} {new_prenume} a fost creat cu id-ul {new_id}.")


    # adaug clientul in banca.json cu balanta 0 lei
    file_banca = open('./bankpackage/banca.json', 'r')
    banca_to_dictionar = json.load(file_banca)
    banca_to_dictionar[f"{new_id}"] = {"nume si prenume": f"{new_nume} {new_prenume}", "balanta": float(0)}
    file_banca.close()

    banca_to_json = json.dumps(banca_to_dictionar, indent=4)

    file_banca = open("./bankpackage/banca.json", "w")
    file_banca.write(banca_to_json)
    file_banca.close()

    # adaug deschiderea de cont in tranzactii.json
    file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
    tranzactii_to_dictionar = json.load(file_tranzactii)
    tranzactii_to_dictionar[new_id] = {}
    tranzactii_to_dictionar[new_id][str(datetime.datetime.now())[:19]] = {
            "Detalii Tranzactie": ["Deschidere cont"],
            "Debit": float(0),
            "Credit": float(0),
            "Balanta": float(0)
        }
    file_tranzactii.close()

    tranzactii_to_json = json.dumps(tranzactii_to_dictionar, indent=4)

    file_tranzactii = open("./bankpackage/tranzactii.json", "w")
    file_tranzactii.write(tranzactii_to_json)
    file_tranzactii.close()
