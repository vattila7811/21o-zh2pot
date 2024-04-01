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

def main():
    pass

if __name__ == '__main__':
    main()
