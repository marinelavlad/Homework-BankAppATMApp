# BankAppATMApp

### Notes: BANK APP ###
# Pentru un client, functionarul de la banca poate modifica_balanta prin 4 optiuni:
    # "1.Depunere numerar",
    # "2.Extragere numerar",
    # "3.Transfer catre un cont din aceeasi banca",
    # "4.Transfer catre un cont de la alta banca",
# Aplicatia stocheaza automat toate tranzactiile, inclusiv deschiderea de cont si tranzactiile la ATM

# Toate tranzactiile asociate unui cont pot fi generate intr-un fisier cu numele clientului, in format .txt
# Aceasta este salvat in folderul "tranzactii"

# Pentru generarea extrasului de cont, se alege o optiune separata din meniu.
# Extrasul de cont se face pt o perioada introdusa de user si se salveaza in folderul "extrase" in format .pdf.

### Notes: ATM APP ###
# aplicația  ATM > genereaza pin/card, schimba pin, interogheaza sold, retragere/depunere bani (totul este logged)
# nu folosește module din aplicația principala pt ca nu am definit functiile cu parametru
# am folosit insa codul de acolo, si tranzactiile de la ATM se regasesc in tranzactii si extras de cont
