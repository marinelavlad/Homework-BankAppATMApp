import datetime
import json


def verifica_balanta():
    file_banca = open("./bankpackage/banca.json", 'r')
    id_client = input("Introdu id_ul clientului:> ")
    banca_to_dictionar = json.load(file_banca)
    gasit = 0
    for cheie_id in banca_to_dictionar:
        if id_client == str(cheie_id):
            gasit = 1
            print(
                f'Soldul clientului {banca_to_dictionar[cheie_id]["nume si prenume"]} cu id-ul {id_client} este {banca_to_dictionar[cheie_id]["balanta"]} lei')
    if gasit == 0:
        print(f'Id-ul {id_client} nu exista! Incearca din nou.')
    file_banca.close()


def modifica_balanta():
    file_banca = open("./bankpackage/banca.json", 'r')
    id_client = input("Introdu id_ul clientului:> ")
    banca_to_dictionar = json.load(file_banca)
    gasit = 0
    for cheie_id in banca_to_dictionar:
        if str(id_client) == str(cheie_id):
            gasit = 1
            print(
                f' Id-ul {id_client} a fost gasit si apartine clientului {banca_to_dictionar[cheie_id]["nume si prenume"]}.')
    if gasit == 0:
        print(f'Id-ul {id_client} nu exista! Incearca din nou.')
    file_banca.close()

    if gasit == 1:
        sm_balanta = [
            "1.Depunere numerar",
            "2.Extragere numerar",
            "3.Transfer catre un cont din aceeasi banca",
            "4.Transfer catre un cont de la alta banca",
            "5.Meniu principal"
        ]
        while True:
            print("-" * 50)
            for sm_b in sm_balanta:
                print(sm_b)
            print("-" * 50)
            optiune = input("Introdu optiunea:> ")
            if optiune == '1':
                # Depunere numerar
                suma = float(input("Introdu suma:> "))
                if suma > 0:
                    file_banca = open("./bankpackage/banca.json", "r")
                    banca_to_dictionar = json.load(file_banca)
                    file_banca.close()

                    noul_credit = float(banca_to_dictionar[id_client]["balanta"]) + suma
                    banca_to_dictionar[id_client]["balanta"] = noul_credit
                    print("Tranzactia(creditarea) a fost efectuata cu succes!")

                    banca_to_json = json.dumps(banca_to_dictionar, indent=4)

                    file_banca = open("./bankpackage/banca.json", "w")
                    file_banca.write(banca_to_json)
                    file_banca.close()

                    file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
                    tranzactii_to_dictionar = json.load(file_tranzactii)
                    tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
                            "Detalii Tranzactie": ["Depunere numerar"],
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
            elif optiune == '2':
                # Extragere numerar
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
                        print("Tranzactia(debitarea) a fost efectuata cu succes!")
                        file_banca.close()

                        banca_to_json = json.dumps(banca_to_dictionar, indent=4)

                        file_banca = open("./bankpackage/banca.json", 'w')
                        file_banca.write(banca_to_json)
                        file_banca.close()

                        file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
                        tranzactii_to_dictionar = json.load(file_tranzactii)
                        tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
                                "Detalii Tranzactie": ["Extragere numerar"],
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

            elif optiune == '3':
                # Transfer catre un cont din aceeasi banca
                id_transfer = input("Introdu id-ul clientului catre care se face transferul:> ")
                file_banca = open("./bankpackage/banca.json", 'r')
                banca_to_dictionar = json.load(file_banca)
                file_banca.close()
                gasit = 0
                for cheie_id in banca_to_dictionar:
                    if id_transfer == str(cheie_id):
                        gasit = 1
                        titular_transfer = banca_to_dictionar[id_transfer]["nume si prenume"]

                if gasit == 0:
                    print(f'Id-ul {id_transfer} nu exista! Incearca din nou.')
                else:
                    print(
                        f'Id-ul {id_transfer} a fost gasit si apartine clientului {titular_transfer}.')
                    # si incep sa fac transferul
                    file_banca = open("./bankpackage/banca.json", "r")
                    banca_to_dictionar = json.load(file_banca)
                    file_banca.close()

                    print(f"Sold disponibil: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
                    suma = float(input("Introdu suma:> "))

                    if suma > 0:
                        file_banca = open("./bankpackage/banca.json", "r")
                        banca_to_dictionar = json.load(file_banca)
                        noul_debit = float(banca_to_dictionar[id_client]['balanta']) - suma
                        noul_credit = float(banca_to_dictionar[id_transfer]['balanta']) + suma
                        file_banca.close()

                        if noul_debit >= 0:
                            file_banca = open("./bankpackage/banca.json", "r")
                            banca_to_dictionar = json.load(file_banca)
                            banca_to_dictionar[id_client]['balanta'] = noul_debit
                            banca_to_dictionar[id_transfer]['balanta'] = noul_credit
                            print("Tranzactiile au fost efectuate cu succes!")
                            file_banca.close()

                            banca_to_json = json.dumps(banca_to_dictionar, indent=4)

                            file_banca = open("./bankpackage/banca.json", 'w')
                            file_banca.write(banca_to_json)
                            file_banca.close()

                            file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
                            tranzactii_to_dictionar = json.load(file_tranzactii)
                            tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
                                    "Detalii Tranzactie": ["Transfer intra-bancar", f"Catre Id_Client: {id_transfer}",
                                                           f"Titular: {titular_transfer}"],
                                    "Debit": suma,
                                    "Credit": float(0),
                                    "Balanta": noul_debit
                                }
                            tranzactii_to_dictionar[f"{id_transfer}"][str(datetime.datetime.now())[:19]] = {
                                    "Detalii Tranzactie": ["Transfer intra-bancar", f"De la Id_Client: {id_client}",
                                                           f"Titular: {banca_to_dictionar[id_client]['nume si prenume']}"],
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
                            print("Tranzactie esuata! Sold insuficient!")
                            print(
                                f"Soldul disponibil este: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
                    else:
                        print("Suma introdusa este < = 0. Incearca din nou, introducand un numar pozitiv!")

            elif optiune == '4':
                # Transfer catre un cont de la alta banca
                file_banca = open("./bankpackage/banca.json", "r")
                banca_to_dictionar = json.load(file_banca)
                print(f"Sold disponibil: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
                file_banca.close()

                suma = float(input("Introdu suma:> "))
                cont_bancar = input("Introdu contul bancar:> ").upper()
                titular_cont = input("Introdu numele titularului de cont:> ").title()
                if suma > 0:
                    file_banca = open("./bankpackage/banca.json", "r")
                    banca_to_dictionar = json.load(file_banca)
                    noul_debit = float(banca_to_dictionar[id_client]['balanta']) - suma
                    file_banca.close()
                    if noul_debit >= 0:
                        file_banca = open("./bankpackage/banca.json", "r")
                        banca_to_dictionar = json.load(file_banca)
                        banca_to_dictionar[id_client]['balanta'] = noul_debit
                        print("Tranzactia(debitarea) a fost efectuata cu succes!")
                        file_banca.close()

                        banca_to_json = json.dumps(banca_to_dictionar, indent=4)

                        file_banca = open("./bankpackage/banca.json", 'w')
                        file_banca.write(banca_to_json)
                        file_banca.close()

                        file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
                        tranzactii_to_dictionar = json.load(file_tranzactii)
                        tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
                                "Detalii Tranzactie": ["Transfer extra-bancar", f"Cont: {cont_bancar}",
                                                       f"Titular: {titular_cont}"],
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
            elif optiune == '5':
                break
            else:
                print("Optiune gresita! Incearca din nou!")