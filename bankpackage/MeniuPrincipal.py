
from bankpackage.NewClients import new_client
from bankpackage.Balanta import verifica_balanta
from bankpackage.Balanta import modifica_balanta
from bankpackage.Tranzactii import afisare_tranzactii
from bankpackage.Extrase import generare_extras

def meniu_principal():
    while True:
        meniu = [
            '1. Adauga un client',
            '2. Verifica balanta',
            '3. Modifica balanta(transfer)',
            '4. Afisare tranzactii',
            '5. Generare extras de cont',
            '6. LogOff'
        ]
        print("*" * 50)
        for sm in meniu:
            print(sm)
        print("*" * 50)
        optiune = input("Introdu optiunea:> ")

        if optiune == '6':
            break
        elif optiune == '1':
            new_client()
        elif optiune == '2':
            verifica_balanta()
        elif optiune == '3':
            modifica_balanta()
        elif optiune == '4':
            afisare_tranzactii()
        elif optiune == '5':
            generare_extras()
        else:
            print("Optiune gresita! Incearca din nou!")