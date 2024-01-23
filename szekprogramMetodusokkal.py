from Szek import Szek

def pldListaban():
    peldany1 = Szek("kék", 3)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)

    szekek = [peldany1, peldany2, peldany3]
    return szekek

def listaki(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])

# rövid verzió:
# listaki(pldListaban())

# hosszú verzió:
# szekLista = pldListaban()
# listaki(szekLista)


def osszegzes(szekek):
    # összegzés tétele
    print("Összesen hány darab székláb van a teremben: ", end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")

def maxKivalasztas(szekek):
    # maximum kiválasztás tétele
    maxIndex = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")

def megszamlalas(szekek):
    # megszámlálás tétele
    print("Hány 4-nél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1
    print(f"{db} db")

def eldontes(szekek):
    print("Van-e piros négy lábú szék: ", end="")
    # eldöntés tétele
    vanE = False
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == str("piros") and szekek[index].labszam == 4:
            vanE = True

    if vanE == True:
        print("van")
    else:
        print("nincs")

szekLista = pldListaban()
listaki(szekLista)
osszegzes(szekLista)
maxKivalasztas(szekLista)
megszamlalas(szekLista)
eldontes(szekLista)
