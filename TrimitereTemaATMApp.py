#### ATMApp.py

# # aplicația  ATM > genereaza pin/card, schimba pin, interogheaza sold, retragere/depunere bani (totul este logged)
# # nu folosește module din aplicația principala pt ca nu am definit functiile cu parametru
# # am folosit insa codul de acolo, si tranzactiile de la ATM se regasesc in tranzactii si extras de cont
#
#
# from atmpackage import emitere_card
# from atmpackage import insert_card
# from atmpackage import meniu_atm
#
# while True:
#     meniu = ["1. Emitere Card Bancar (cu PIN initial)",
#              "2. Introducere card in ATM",
#              "3. Exit"]
#     print("="*40)
#     for sm in meniu:
#         print(sm)
#     print("="*40)
#     optiune = input("Introdu optiunea ta:> ")
#     if optiune == "1":
#         emitere_card.card_bancar()
#     elif optiune == "2":
#
#         print("Bine ai venit la ATM_App by MariVlad!\nIntrodu datele cardului:")
#         while True:
#             nr_card = input("Numar card:> ")
#             pin = input("PIN:> ")
#
#             autorizat = False
#
#             if insert_card.introducere_card(nr_card, pin) == True:
#                 autorizat = True
#             elif insert_card.introducere_card(nr_card, pin) == 'numar card gresit':
#                 print("Numarul cardului nu exista. Incearca din nou.")
#                 continue
#             elif insert_card.introducere_card(nr_card, pin) == 'pin gresit':
#                 print("PIN gresit. Incearca din nou!")
#             else:
#                 pass
#             if autorizat == True:
#                 meniu_atm.meniu_principal(nr_card)
#
#     elif optiune == "3":
#         break
#     else:
#         print("Optiune invalida! Incearca din nou.")

#........................................................................................



#in acelasi folder in care avem BankApp am facut un folder: "atmpackage" care contine:

#======================================================================================
########## __init__.py

# from atmpackage import emitere_card
# from atmpackage import insert_card
# from atmpackage import meniu_atm
# from atmpackage import modificare_pin
# from atmpackage import operatiuni

#======================================================================================



#======================================================================================
########### emitere_card.py

# import json
# import datetime
# import random
#
#
# def card_bancar():
#     id_client = input("Introdu id_ul clientului pentru care se doreste emiterea cardului bancar:> ")
#     file_clienti = open(
#         "./bankpackage/clients.json", 'r')
#     clienti_to_dictionar = json.load(file_clienti)
#     gasit = 0
#     for cheie_id in clienti_to_dictionar:
#         if str(id_client) == str(cheie_id):
#             gasit = 1
#             nume_client = clienti_to_dictionar[id_client]["nume"] + " " + clienti_to_dictionar[id_client]["prenume"]
#             print(
#                 f'Id-ul {id_client} a fost gasit si apartine clientului {nume_client}.')
#     if gasit == 0:
#         print(f'Id-ul {id_client} nu exista! Incearca din nou.')
#     file_clienti.close()
#
#     if gasit == 1:
#         file_card = open("./atmpackage/card.json", "r")
#         card_to_dict = json.load(file_card)
#         file_card.close()
#
#         # generez un nr de card unic
#         flag = True
#         while flag:
#             numar_card = ""
#             for i in range(0, 16):
#                 numar_card += str(random.randint(0, 9))
#             unic = 1
#             for cheie_card in card_to_dict:
#                 if cheie_card == numar_card:
#                     unic = 0
#             if unic == 1:
#                 flag = False
#         cvc = ""
#         for i in range(0, 3):
#             cvc += str(random.randint(0, 9))
#         pin = ""
#         for i in range(0, 4):
#             pin += str(random.randint(0, 9))
#
#         # emit un card nou pt id-ul clientului ales
#         # salvez in fisier card.json unde nr de card generat este cheie
#         card_to_dict[numar_card] = {
#             "id_client": id_client,
#             "titular card": nume_client,
#             "data expirare": str(datetime.datetime.now())[5:7] + "/" + str(int(str(datetime.datetime.now())[:4]) + 2),
#             "cvc": cvc,
#             "pin": pin,
#             "moneda": "RON"
#         }
#         print(f"\nCardul a fost emis cu succes:\nNumar card: {numar_card}\nTitular card: {nume_client}\nData expirare:{str(datetime.datetime.now())[5:7] + '/' + str(int(str(datetime.datetime.now())[:4]) + 2)}\nCVC:{cvc}\nPIN initial:{pin}\n")
#         card_to_json = json.dumps(card_to_dict, indent=4)
#
#         file_card = open("./atmpackage/card.json", "w")
#         file_card.write(card_to_json)
#         file_card.close()

#======================================================================================




#======================================================================================
######### insert_card.py

# import json
#
# def introducere_card(nr_card, pin):
#     file_card = open("./atmpackage/card.json", "r")
#     card_to_dict = json.load(file_card)
#     file_card.close()
#     gasit = 0
#     for cheie_nrcard in card_to_dict:
#         if cheie_nrcard == nr_card:
#             gasit = 1
#             if card_to_dict[cheie_nrcard]["pin"] == pin:
#                 print(f"Buna {card_to_dict[cheie_nrcard]['titular card']}! Te-ai conectat cu succes la ATM_App :-)")
#                 return True
#             else:
#                 return 'pin gresit'
#     if gasit == 0:
#         return 'numar card gresit'
#     else:
#         pass

#======================================================================================



#======================================================================================
######## meniu_atm.py

# from atmpackage import modificare_pin
# from atmpackage import operatiuni
#
# def meniu_principal(nr_card):
#     while True:
#         meniu_pr = [
#             "1. Modificare PIN",
#             "2. Interogare sold",
#             "3. Retragere numerar",
#             "4. Depunere numerar",
#             "5. Exit"
#         ]
#         print("-" * 50)
#         for sm in meniu_pr:
#             print(sm)
#         print("-" * 50)
#
#         optiune = input("Introdu optiunea:> ")
#
#         if optiune == "1":
#             modificare_pin.new_pin(nr_card)
#         elif optiune == "2":
#             operatiuni.interogare_sold(nr_card)
#         elif optiune == "3":
#             operatiuni.retragere_numerar(nr_card)
#         elif optiune == "4":
#             operatiuni.depunere_numerar(nr_card)
#         elif optiune == "5":
#             break
#         else:
#             print("Optiune invalida! Incearca din nou!")

#======================================================================================



#======================================================================================
#### modificare_pin.py

# import json
#
# def new_pin(nr_card):
#     noul_pin = input("Introdu noul cod PIN format din 4 cifre:\n> ")
#     verificare_noul_pin = input("Reintrodu noul cod PIN pentru verificare:\n> ")
#     ok = 0
#     if len(noul_pin) == 4:
#         if noul_pin == verificare_noul_pin:
#             ok = 1
#         else:
#             print("Cele doua coduri PIN nu coincid. Incearca din nou!")
#     else:
#         print("Codul PIN trebuie sa aiba exact 4 cifre. Incearca din nou!")
#
#     if ok == 1:
#         file_card = open("./atmpackage/card.json.json",
#                          "r")
#         card_to_dict = json.load(file_card)
#         file_card.close()
#
#         card_to_dict[nr_card]["pin"] = noul_pin
#         print("Noul PIN a fost salvat cu succes!")
#
#         card_to_json = json.dumps(card_to_dict, indent=4)
#
#         file_card = open("./atmpackage/card.json",
#                          "w")
#         file_card.write(card_to_json)
#         file_card.close()

#======================================================================================


#======================================================================================
####### operatiuni.py

# import json
# import datetime
#
#
# def interogare_sold(nr_card):
#     file_card = open("./atmpackage/card.json", "r")
#     card_to_dict = json.load(file_card)
#     file_card.close()
#
#     id_client = card_to_dict[nr_card]["id_client"]
#
#     file_banca = open("./bankpackage/banca.json", "r")
#     banca_to_dict = json.load(file_banca)
#     file_banca.close()
#
#     print(f"Sold disponibil: {banca_to_dict[id_client]['balanta']} lei")
#
#
#
# def retragere_numerar(nr_card):
#     file_card = open("./atmpackage/card.json", "r")
#     card_to_dict = json.load(file_card)
#     file_card.close()
#
#     id_client = card_to_dict[nr_card]["id_client"]
#
#     # Extragere numerar de la ATM
#     file_banca = open("./bankpackage/banca.json", "r")
#     banca_to_dictionar = json.load(file_banca)
#     file_banca.close()
#     print(f"Sold disponibil: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
#     suma = float(input("Introdu suma:> "))
#     if suma > 0:
#         file_banca = open("./bankpackage/banca.json", "r")
#         banca_to_dictionar = json.load(file_banca)
#         file_banca.close()
#         noul_debit = float(banca_to_dictionar[id_client]['balanta']) - suma
#         if noul_debit >= 0:
#             file_banca = open("./bankpackage/banca.json", "r")
#             banca_to_dictionar = json.load(file_banca)
#             banca_to_dictionar[id_client]['balanta'] = noul_debit
#             print("Retragere numerar efectuata cu succes!\nNu uita sa iei banii din bancomat!")
#             file_banca.close()
#
#             banca_to_json = json.dumps(banca_to_dictionar, indent=4)
#
#             file_banca = open("./bankpackage/banca.json", 'w')
#             file_banca.write(banca_to_json)
#             file_banca.close()
#
#             file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
#             tranzactii_to_dictionar = json.load(file_tranzactii)
#             tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
#                 "Detalii Tranzactie": ["Retragere numerar de la ATM"],
#                 "Debit": suma,
#                 "Credit": float(0),
#                 "Balanta": noul_debit
#             }
#             file_tranzactii.close()
#
#             tranzactii_to_json = json.dumps(tranzactii_to_dictionar, indent=4)
#
#             file_tranzactii = open('./bankpackage/tranzactii.json', 'w')
#             file_tranzactii.write(tranzactii_to_json)
#             file_tranzactii.close()
#         else:
#             print("Tranzactie esuata! Sold insuficient!")
#             print(f"Soldul disponibil este: {float(banca_to_dictionar[id_client]['balanta'])}lei.")
#     else:
#         print("Suma introdusa este < = 0. Incearca din nou, introducand un numar pozitiv!")
#
#
# def depunere_numerar(nr_card):
#     file_card = open("./atmpackage/card.json", "r")
#     card_to_dict = json.load(file_card)
#     file_card.close()
#
#     id_client = card_to_dict[nr_card]["id_client"]
#
#     # Depunere numerar la ATM
#     suma = float(input("Introdu suma:> "))
#     if suma > 0:
#         file_banca = open("./bankpackage/banca.json", "r")
#         banca_to_dictionar = json.load(file_banca)
#         file_banca.close()
#
#         noul_credit = float(banca_to_dictionar[id_client]["balanta"]) + suma
#         banca_to_dictionar[id_client]["balanta"] = noul_credit
#         print("Depunere numerar realizata cu succes! Va multumim!")
#
#         banca_to_json = json.dumps(banca_to_dictionar, indent=4)
#
#         file_banca = open("./bankpackage/banca.json", "w")
#         file_banca.write(banca_to_json)
#         file_banca.close()
#
#         file_tranzactii = open('./bankpackage/tranzactii.json', 'r')
#         tranzactii_to_dictionar = json.load(file_tranzactii)
#         tranzactii_to_dictionar[f"{id_client}"][str(datetime.datetime.now())[:19]] = {
#             "Detalii Tranzactie": ["Depunere numerar la ATM"],
#             "Debit": float(0),
#             "Credit": suma,
#             "Balanta": noul_credit
#         }
#         file_tranzactii.close()
#
#         tranzactii_to_json = json.dumps(tranzactii_to_dictionar, indent=4)
#
#         file_tranzactii = open('./bankpackage/tranzactii.json', 'w')
#         file_tranzactii.write(tranzactii_to_json)
#         file_tranzactii.close()
#     else:
#         print("Suma introdusa este < = 0. Incearca din nou!")

#======================================================================================
##### card.json

# {
#     "4157764069644085": {
#         "id_client": "2",
#         "titular card": "Gheorghe Paul",
#         "data expirare": "04/2023",
#         "cvc": "584",
#         "pin": "8434",
#         "moneda": "RON"
#     },
#     "0155503764689560": {
#         "id_client": "1",
#         "titular card": "Vlad Ionut",
#         "data expirare": "04/2023",
#         "cvc": "747",
#         "pin": "7169",
#         "moneda": "RON"
#     }
# }





