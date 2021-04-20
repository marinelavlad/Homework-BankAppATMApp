### Bank Application

### Notes: ###
# Pentru un client, functionarul de la banca poate modifica_balanta prin 4 optiuni:
    # "1.Depunere numerar",
    # "2.Extragere numerar",
    # "3.Transfer catre un cont din aceeasi banca",
    # "4.Transfer catre un cont de la alta banca",
# Aplicatia stocheaza automat toate tranzactiile, inclusiv deschiderea de cont

# Toate tranzactiile asociate unui cont pot fi generate intr-un fisier cu numele clientului, in format .txt
# Aceasta este salvat in folderul "tranzactii"

# Pentru generarea extrasului de cont, se alege o optiune separata din meniu.
# Extrasul de cont se face pt o perioada introdusa de user si se salveaza in folderul "extrase" in format .pdf.

from bankpackage.Auth import login
from bankpackage.MeniuPrincipal import meniu_principal



print("Bank Application OnLine...")
while True:
    user = input("username:\n> ")
    password = input("password:\n> ")

    autorizat = False

    if login(user, password) == True:
        autorizat = True
    elif login(user, password) == 'username gresit':
        print("Utilizatorul nu exista. Incearca din nou.")
        continue
    elif login(user, password) == 'password gresit':
        print("Parola gresita. Incearca din nou!")
    else:
        pass
    if autorizat == True:
        meniu_principal()