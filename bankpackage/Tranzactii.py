import json


def afisare_tranzactii():
    id_client = input("Introdu id_ul clientului:> ")
    file_clienti = open("./bankpackage/clients.json", 'r')
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
        file_tranzactii = open("./bankpackage/tranzactii.json", "r")
        tranzactii_to_dictionar = json.load(file_tranzactii)
        file_tranzactii.close()

        ################# creez mai intai antetul:

        file_all_tranz = open(f"./tranzactii/{id_client}.txt", "w")

        file_all_tranz.write(
            f"ID_Client: {id_client}\n"
            f"Nume si prenume: {clienti_to_dictionar[id_client]['nume']} {clienti_to_dictionar[id_client]['prenume']}\n"
            f"Telefon: {clienti_to_dictionar[id_client]['telefon']}\n"
            f"Oras: {clienti_to_dictionar[id_client]['oras']}\n"
            f"Moneda:RON\n\n")
        file_all_tranz.write("-" * 120 + '\n')
        file_all_tranz.write(
            f"Data{(15 - len('Data')) * ' '}\tDetalii Tranzactie{(50 - len('Detalii Tranzactie')) * ' '}\tDebit{(15 - len('Debit')) * ' '}\tCredit{(15 - len('Credit')) * ' '}\tBalanta{(15 - len('Balanta')) * ' '}\n")
        file_all_tranz.write("-" * 120 + '\n\n')

        ################# includ apoi toate tranzactiile:
        for cheie_data in tranzactii_to_dictionar[id_client]:
            file_all_tranz.write(
                f"{cheie_data[:10]}{(15 - len(cheie_data[:10])) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][0]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][0])) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Debit']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Debit']))) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Credit']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Credit']))) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Balanta']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Balanta']))) * ' '}\n")
            if len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie']) == 3:
                file_all_tranz.write(
                    f"{''}{(15 - len('')) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][1]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][1])) * ' '}\t{''}{(15 - len('')) * ' '}\t{''}{(15 - len('')) * ' '}\t{''}{(15 - len('')) * ' '}\n")
                file_all_tranz.write(
                    f"{''}{(15 - len('')) * ' '}\t{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][2]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][2])) * ' '}\t{''}{(15 - len('')) * ' '}\t{''}{(15 - len('')) * ' '}\t{''}{(15 - len('')) * ' '}\n")
        file_all_tranz.close()

        ## afisez si in program:
        file_all_tranz = open(f"./tranzactii/{int(id_client)}.txt", "r")
        print("\n")
        print("=" * 120)
        print(file_all_tranz.read())
        print("=" * 120)
        print("\n")
        file_all_tranz.close()