from atmpackage import modificare_pin
from atmpackage import operatiuni

def meniu_principal(nr_card):
    while True:
        meniu_pr = [
            "1. Modificare PIN",
            "2. Interogare sold",
            "3. Retragere numerar",
            "4. Depunere numerar",
            "5. Exit"
        ]
        print("-" * 50)
        for sm in meniu_pr:
            print(sm)
        print("-" * 50)

        optiune = input("Introdu optiunea:> ")

        if optiune == "1":
            modificare_pin.new_pin(nr_card)
        elif optiune == "2":
            operatiuni.interogare_sold(nr_card)
        elif optiune == "3":
            operatiuni.retragere_numerar(nr_card)
        elif optiune == "4":
            operatiuni.depunere_numerar(nr_card)
        elif optiune == "5":
            break
        else:
            print("Optiune invalida! Incearca din nou!")