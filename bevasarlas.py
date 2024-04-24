# Feladat: Írj programot, ami segít megszervezni a bevásárlást!

# Az akciós termékek neveit és árait egy másik program már összegyűjtötte a boltoktól.
# Az árak az 'akciok.json' fájlban vannak egy listában.
# Minden listaelem egy boltnak az akcióit tartalmazza egy {termeknev:ar} dictionary-ben.
# Ugyanaz a termék több bolt akciói között is szerepelhet, de nem biztos, hogy minden
# bolt kinálatában szerepel.

# A program határozza meg minden terméknek a legolcsóbb árát.
# Ezeket írja ki tetszőleges sorrendben, de minden terméket csak egyszer.
# A megadott fájlra ez a helyes megoldás, és az elvárt kimeneti formátum:
'''
csirkemell: 780 Ft
csirkefarhat: 240 Ft
cukor: 350 Ft
kalacs: 460 Ft
kenyer: 320 Ft
mez: 650 Ft
tej: 340 Ft
tejfol: 160 Ft
'''

# Ezután kérje be a felhasználótól a bevásárlólistáját.
# Bemeneti formátum: szóközzel elválasztott terméknevek, pl.:
'tej kenyer cukor'

# Írja ki, hogy ha egy boltban akarjuk megvenni az összes terméket a listáról,
# akkor az melyik boltban lesz a legolcsóbb, és mennyibe fog kerülni.
# A megadott példára:
'3. boltban 1080 Ft'
# Ha nincs olyan bolt, ahol egy helyen megvehető lenne az összes kívánt termék,
# akkor ezt írja ki:
'Nincs olyan bolt, ahol minden termek kaphato!'
# Az is ide tartozik, ha olyan termék neve lett megadva, amelyik egyik boltban
# sem kapható.

# A beolvasás, a legolcsóbb árak kiszámítása és a legolcsóbb bolt keresése
# 3 külön függvényben legyen megoldva!
# (Ezen felül lehetnek további segédfüggvények.)


import json
import math

AKCIO = dict[str, int]
AKCIOK = list[AKCIO]

BAD_VALUE = -1

DBNEV = "akciok.json"

def load_akciok() -> AKCIOK:
    akciok : AKCIOK = []
    with open(DBNEV, "r", encoding="utf-8") as jsonfile:
        akciok = json.load(jsonfile)
    return akciok
    

def collect_cheapest(akciok: AKCIOK) -> AKCIO:
    legolcsobb : AKCIO = {}
    for akcio in akciok:
        for etel, ar in akcio.items():
            olcsoar = legolcsobb.get(etel, 0)
            if olcsoar == 0 or ar < olcsoar:
                legolcsobb[etel] = ar
    return legolcsobb

def print_lista(etellista: AKCIO):
    for etel, ar in etellista.items():
        print(f"{etel}: {ar} Ft")


def sum_shopping(ajanlat: AKCIO, bevasarlolista : list[str]) -> int:
    db = 0
    osszar =  0
    for etel in bevasarlolista:
        ar = ajanlat.get(etel, BAD_VALUE)
        if ar != BAD_VALUE:
            db +=1
            osszar += ar
    if db == len(bevasarlolista):
        return osszar
    return math.inf


def search_cheapest_store(akciok: AKCIOK, etellista: list[str]) -> int:
    arak = [sum_shopping(akcio, etellista) for akcio in akciok ]
    
    if min(arak) < math.inf:
        return arak.index(min(arak))
    return BAD_VALUE 
    

def print_offer(akciok: AKCIOK, etellista: list[str], sorszam: int):
    if sorszam == BAD_VALUE:
        print('Nincs olyan bolt, ahol minden termek kaphato!')
    else: 
        print(f'{sorszam + 1}. boltban {sum_shopping(akciok[sorszam], etellista)} Ft')


def main():
    akciok = load_akciok()
    print_lista(collect_cheapest(akciok))

    etellista = input("Kérem a bevásárlólistát szóközökkel elválasztva: ").split()
    olcsobolt = search_cheapest_store(akciok, etellista)
    print_offer(akciok, etellista, olcsobolt)

main()
