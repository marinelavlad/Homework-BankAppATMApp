import json

def new_pin(nr_card):
    noul_pin = input("Introdu noul cod PIN format din 4 cifre:\n> ")
    verificare_noul_pin = input("Reintrodu noul cod PIN pentru verificare:\n> ")
    ok = 0
    if len(noul_pin) == 4:
        if noul_pin == verificare_noul_pin:
            ok = 1
        else:
            print("Cele doua coduri PIN nu coincid. Incearca din nou!")
    else:
        print("Codul PIN trebuie sa aiba exact 4 cifre. Incearca din nou!")

    if ok == 1:
        file_card = open("./atmpackage/card.json",
                         "r")
        card_to_dict = json.load(file_card)
        file_card.close()

        card_to_dict[nr_card]["pin"] = noul_pin
        print("Noul PIN a fost salvat cu succes!")

        card_to_json = json.dumps(card_to_dict, indent=4)

        file_card = open("./atmpackage/card.json",
                         "w")
        file_card.write(card_to_json)
        file_card.close()