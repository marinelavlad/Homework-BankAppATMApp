# aplicația  ATM > genereaza pin/card, schimba pin, interogheaza sold, retragere/depunere bani (totul este logged)
# nu folosește module din aplicația principala pt ca nu am definit functiile cu parametru
# am folosit insa codul de acolo, si tranzactiile de la ATM se regasesc in tranzactii si extras de cont


from atmpackage import emitere_card
from atmpackage import insert_card
from atmpackage import meniu_atm

while True:
    meniu = ["1. Emitere Card Bancar (cu PIN initial)",
             "2. Introducere card in ATM",
             "3. Exit"]
    print("="*40)
    for sm in meniu:
        print(sm)
    print("="*40)
    optiune = input("Introdu optiunea ta:> ")
    if optiune == "1":
        emitere_card.card_bancar()
    elif optiune == "2":

        print("Bine ai venit la ATM_App by MariVlad!\nIntrodu datele cardului:")
        while True:
            nr_card = input("Numar card:> ")
            pin = input("PIN:> ")

            autorizat = False

            if insert_card.introducere_card(nr_card, pin) == True:
                autorizat = True
            elif insert_card.introducere_card(nr_card, pin) == 'numar card gresit':
                print("Numarul cardului nu exista. Incearca din nou.")
                continue
            elif insert_card.introducere_card(nr_card, pin) == 'pin gresit':
                print("PIN gresit. Incearca din nou!")
            else:
                pass
            if autorizat == True:
                meniu_atm.meniu_principal(nr_card)

    elif optiune == "3":
        break
    else:
        print("Optiune invalida! Incearca din nou.")