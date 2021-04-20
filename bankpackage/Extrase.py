import json
import datetime
import time
from reportlab.pdfgen.canvas import Canvas


def generare_extras():
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

        ### aleg intervalul pentru care sa generez extrasul
        for cheie_data in tranzactii_to_dictionar[id_client].keys():
            data_deschidere_cont = cheie_data[8:10] + "/" + cheie_data[5:7] + "/" + cheie_data[:4]
            break
        data_acum = str(datetime.datetime.now())[8:10] + "/" + str(datetime.datetime.now())[5:7] + "/" + str(datetime.datetime.now())[:4]
        new_data_cont = time.strptime(data_deschidere_cont, "%d/%m/%Y")
        new_data_acum = time.strptime(data_acum, "%d/%m/%Y")

        print(f"Poti genera un extras de cont din perioada maxima: {data_deschidere_cont} - {data_acum}.")

        data_inceput = input("Introdu data de inceput (format necesar: dd/mm/yyyy):\n> ")
        data_sfarsit = input("Introdu data de sfarsit (format necesar: dd/mm/yyyy):\n> ")
        new_data_inceput = time.strptime(data_inceput, "%d/%m/%Y")
        new_data_sfarsit = time.strptime(data_sfarsit, "%d/%m/%Y")


        if new_data_inceput < new_data_cont or new_data_sfarsit > new_data_acum:
            print("Intervalul ales nu este introdus corect. Incearca din nou!")
            print(
                f"Atentie! Poti genera un extras de cont din perioada maxima: {data_deschidere_cont} - {data_acum}.")
        else:
            #### incep generarea extrasului

            ### creez mai intai antetul:
            ora = datetime.datetime.now().strftime("%Y%m%d%H-%M-%S")
            canvas_extras = Canvas(f"./extrase/{id_client}_{ora}.pdf")
            canvas_extras.setFont("Courier", 11)

            canvas_extras.drawString(30, 800, f"ID_Client: {id_client}")
            canvas_extras.drawString(30, 775, f"Nume si prenume: {clienti_to_dictionar[id_client]['nume']} {clienti_to_dictionar[id_client]['prenume']}")
            canvas_extras.drawString(30, 750, f"Telefon: {clienti_to_dictionar[id_client]['telefon']}")
            canvas_extras.drawString(30, 725, f"Oras: {clienti_to_dictionar[id_client]['oras']}")
            canvas_extras.drawString(30, 700, f"Moneda:RON")

            canvas_extras.setFont("Courier", 8)

            canvas_extras.drawString(30, 650, "-" * 110)
            canvas_extras.drawString(30, 625, f"Data{(15 - len('Data')) * ' '}Detalii Tranzactie{(50 - len('Detalii Tranzactie')) * ' '}Debit{(15 - len('Debit')) * ' '}Credit{(15 - len('Credit')) * ' '}Balanta{(15 - len('Balanta')) * ' '}")
            canvas_extras.drawString(30, 600, "-" * 110)

            ################# includ apoi toate tranzactiile:
            tranzactii = 0
            y = 575
            for cheie_data in tranzactii_to_dictionar[id_client]:
                # verific daca cheia se afla in intervalul dat
                # daca da, o adaug la extras
                data_cheie = cheie_data[8:10] + "/" + cheie_data[5:7] + "/" + cheie_data[:4]
                new_data_cheie = time.strptime(data_cheie, "%d/%m/%Y")
                if new_data_inceput <= new_data_cheie:
                    if new_data_cheie <= new_data_sfarsit:
                        tranzactii = 1
                        canvas_extras.drawString(30, y, f"{cheie_data[:10]}{(15 - len(cheie_data[:10])) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][0]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][0])) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Debit']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Debit']))) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Credit']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Credit']))) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Balanta']}{(15 - len(str(tranzactii_to_dictionar[id_client][cheie_data]['Balanta']))) * ' '}")
                        y -= 20
                        if len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie']) == 3:
                            canvas_extras.drawString(30, y, f"{''}{(15 - len('')) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][1]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][1])) * ' '}{''}{(15 - len('')) * ' '}{''}{(15 - len('')) * ' '}{''}{(15 - len('')) * ' '}")
                            y -= 20
                            canvas_extras.drawString(30, y, f"{''}{(15 - len('')) * ' '}{tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][2]}{(50 - len(tranzactii_to_dictionar[id_client][cheie_data]['Detalii Tranzactie'][2])) * ' '}{''}{(15 - len('')) * ' '}{''}{(15 - len('')) * ' '}{''}{(15 - len('')) * ' '}")
                            y -= 20
            if tranzactii == 0:
                canvas_extras.drawString(30, y, "Nu exista tranzactii realizate in perioada selectata!")

            canvas_extras.drawString(100, 60, "Data:")
            canvas_extras.drawString(100, 35, f"{data_acum}")

            canvas_extras.drawString(400, 60, "Semnat,")
            canvas_extras.setFont("Times-BoldItalic", 8)
            canvas_extras.drawString(430, 35, "BankApp by MariVlad")

            canvas_extras.save()

            ## afisez si in program:
            print(f"Fisierul {id_client}_{ora}.pdf a fost generat si sa gaseste in folderul: ./extrase/")
