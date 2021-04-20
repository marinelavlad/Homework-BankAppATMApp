#  >>  https://pastebin.com/5nEu4uzU

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


### ARHITECTURA TEMA: ###
# Fisierul principal
            # BankApp.py        >>> https://pastebin.com/33SZqsbR
# 2 foldere: "tranzactii" si "extrase"
# un folder numit bankpackage a carui structura este mai jos:


# care contine fisiere .py:
    # __init__.py cu codul:
            # from bankpackage import Auth
            # from bankpackage import MeniuPrincipal
            # from bankpackage import Balanta
            # from bankpackage import Extrase
            # from bankpackage import NewClients
            # from bankpackage import Tranzactii
    # Auth.py           >>> https://pastebin.com/BtUPitTA
    # MeniuPrincipal.py >>> https://pastebin.com/u4k8W0Lk
    # NewClients.py     >>> https://pastebin.com/MiAc7WcG
    # Balanta.py        >>> https://pastebin.com/C9ZmZ9Jc
    # Tranzactii.py     >>> https://pastebin.com/PAJMGLNi
    # Extrase.py        >>> https://pastebin.com/1Kww22FS

# fisiere .json (dupa testare app de catre mine)
    #auth.json          >>>
{
    "1": {
        "mari": "123"
    },
    "2": {
        "bogdan": "456"
    },
    "3": {
        "vlad": "789"
    }
}
    # banca.json        >>>
{
    "1": {
        "nume si prenume": "Vlad Ionut",
        "balanta": 237.0
    },
    "2": {
        "nume si prenume": "Gheorghe Paul",
        "balanta": 754.0
    },
    "3": {
        "nume si prenume": "Popescu Mihai",
        "balanta": 225.0
    }
}
    # clients.json      >>>
{
    "1": {
        "nume": "Vlad",
        "prenume": "Ionut",
        "telefon": "0741258369",
        "oras": "Bucuresti"
    },
    "2": {
        "nume": "Gheorghe",
        "prenume": "Paul",
        "telefon": "0795684325",
        "oras": "Pitesti"
    },
    "3": {
        "nume": "Popescu",
        "prenume": "Mihai",
        "telefon": "0789654123",
        "oras": "Valcea"
    }
}
    # tranzactii.json       >>>
{
    "1": {
        "2021-04-10 21:42:57": {
            "Detalii Tranzactie": [
                "Deschidere cont"
            ],
            "Debit": 0.0,
            "Credit": 0.0,
            "Balanta": 0.0
        },
        "2021-04-10 21:43:28": {
            "Detalii Tranzactie": [
                "Depunere numerar"
            ],
            "Debit": 0.0,
            "Credit": 500.0,
            "Balanta": 500.0
        },
        "2021-04-10 21:43:31": {
            "Detalii Tranzactie": [
                "Extragere numerar"
            ],
            "Debit": 150.0,
            "Credit": 0.0,
            "Balanta": 350.0
        },
        "2021-04-10 21:43:40": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "Catre Id_Client: 2",
                "Titular: Gheorghe Paul"
            ],
            "Debit": 50.0,
            "Credit": 0.0,
            "Balanta": 300.0
        },
        "2021-04-10 21:44:09": {
            "Detalii Tranzactie": [
                "Transfer extra-bancar",
                "Cont: RO45RZBR000011112222",
                "Titular: Ion Matei"
            ],
            "Debit": 100.0,
            "Credit": 0.0,
            "Balanta": 200.0
        },
        "2021-04-11 15:06:59": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "De la Id_Client: 2",
                "Titular: Gheorghe Paul"
            ],
            "Debit": 0.0,
            "Credit": 186.0,
            "Balanta": 386.0
        },
        "2021-04-14 14:17:50": {
            "Detalii Tranzactie": [
                "Extragere numerar"
            ],
            "Debit": 50.0,
            "Credit": 0.0,
            "Balanta": 336.0
        },
        "2021-04-14 14:18:01": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "Catre Id_Client: 2",
                "Titular: Gheorghe Paul"
            ],
            "Debit": 221.0,
            "Credit": 0.0,
            "Balanta": 115.0
        },
        "2021-04-14 14:43:22": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "De la Id_Client: 3",
                "Titular: Popescu Mihai"
            ],
            "Debit": 0.0,
            "Credit": 122.0,
            "Balanta": 237.0
        }
    },
    "2": {
        "2021-04-10 21:43:16": {
            "Detalii Tranzactie": [
                "Deschidere cont"
            ],
            "Debit": 0.0,
            "Credit": 0.0,
            "Balanta": 0.0
        },
        "2021-04-10 21:43:40": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "De la Id_Client: 1",
                "Titular: Vlad Ionut"
            ],
            "Debit": 0.0,
            "Credit": 50.0,
            "Balanta": 50.0
        },
        "2021-04-11 15:06:42": {
            "Detalii Tranzactie": [
                "Depunere numerar"
            ],
            "Debit": 0.0,
            "Credit": 800.0,
            "Balanta": 850.0
        },
        "2021-04-11 15:06:48": {
            "Detalii Tranzactie": [
                "Extragere numerar"
            ],
            "Debit": 250.0,
            "Credit": 0.0,
            "Balanta": 600.0
        },
        "2021-04-11 15:06:59": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "Catre Id_Client: 1",
                "Titular: Vlad Ionut"
            ],
            "Debit": 186.0,
            "Credit": 0.0,
            "Balanta": 414.0
        },
        "2021-04-14 14:16:27": {
            "Detalii Tranzactie": [
                "Depunere numerar"
            ],
            "Debit": 0.0,
            "Credit": 320.0,
            "Balanta": 734.0
        },
        "2021-04-14 14:16:40": {
            "Detalii Tranzactie": [
                "Extragere numerar"
            ],
            "Debit": 17.0,
            "Credit": 0.0,
            "Balanta": 717.0
        },
        "2021-04-14 14:17:29": {
            "Detalii Tranzactie": [
                "Transfer extra-bancar",
                "Cont: RO01INGB0000141425253636",
                "Titular: Camataru Fane"
            ],
            "Debit": 184.0,
            "Credit": 0.0,
            "Balanta": 533.0
        },
        "2021-04-14 14:18:01": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "De la Id_Client: 1",
                "Titular: Vlad Ionut"
            ],
            "Debit": 0.0,
            "Credit": 221.0,
            "Balanta": 754.0
        }
    },
    "3": {
        "2021-04-14 14:42:47": {
            "Detalii Tranzactie": [
                "Deschidere cont"
            ],
            "Debit": 0.0,
            "Credit": 0.0,
            "Balanta": 0.0
        },
        "2021-04-14 14:43:06": {
            "Detalii Tranzactie": [
                "Depunere numerar"
            ],
            "Debit": 0.0,
            "Credit": 450.0,
            "Balanta": 450.0
        },
        "2021-04-14 14:43:14": {
            "Detalii Tranzactie": [
                "Extragere numerar"
            ],
            "Debit": 78.0,
            "Credit": 0.0,
            "Balanta": 372.0
        },
        "2021-04-14 14:43:22": {
            "Detalii Tranzactie": [
                "Transfer intra-bancar",
                "Catre Id_Client: 1",
                "Titular: Vlad Ionut"
            ],
            "Debit": 122.0,
            "Credit": 0.0,
            "Balanta": 250.0
        },
        "2021-04-14 14:44:00": {
            "Detalii Tranzactie": [
                "Transfer extra-bancar",
                "Cont: RO14BRDB1414585896963232",
                "Titular: Gheorghe Vasile"
            ],
            "Debit": 25.0,
            "Credit": 0.0,
            "Balanta": 225.0
        }
    }
}