import json

def introducere_card(nr_card, pin):
    file_card = open("./atmpackage/card.json", "r")
    card_to_dict = json.load(file_card)
    file_card.close()
    gasit = 0
    for cheie_nrcard in card_to_dict:
        if cheie_nrcard == nr_card:
            gasit = 1
            if card_to_dict[cheie_nrcard]["pin"] == pin:
                print(f"Buna {card_to_dict[cheie_nrcard]['titular card']}! Te-ai conectat cu succes la ATM_App :-)")
                return True
            else:
                return 'pin gresit'
    if gasit == 0:
        return 'numar card gresit'
    else:
        pass