#!/usr/bin/env python3

def fájlból_lista(fájlnév):
    lista = []
    with open(fájlnév, encoding='utf-8') as forrásfájl:
        for sor in forrásfájl:
            sor = sor.strip().split()
            # A lista végére egy újabb szótárat helyezünk.
            # Dolgozhatnánk listák listájával is, ilyen megoldást az előző
            # feladathoz tartozó, eredet.py programban mutatunk be.
            lista.append({'név': sor[0], 'szám': int(sor[1]), 'nem': sor[2]})
    return lista

def gyakoriság_szerint_rendez(lista):
    for külső_index in range(len(lista)-1):
        # A külső_index előttiek már rendezve vannak.
        legnagyobb_indexe = külső_index 
            # Végignézzük egyesével a még hátralévő elemeket.
            # Megkeressük, hogy melyik közülük a legnagyobb.
        for belső_index in range(külső_index+1, len(lista)):
            if lista[legnagyobb_indexe]['szám'] < lista[belső_index]['szám']:
                legnagyobb_indexe = belső_index
        lista[külső_index], lista[legnagyobb_indexe] = lista[legnagyobb_indexe], lista[külső_index]
    return lista

def nem_szerint_válogat(lista, nem):
    válogatott_nevek = []
    for elem in lista:
        if elem['nem'] == nem:
            válogatott_nevek.append(elem['név'])
    return válogatott_nevek

def neveket_fájlba_ír(névlista, fájlnév):
    with open(fájlnév, 'w', encoding='utf-8') as célfájl:
        for név in névlista:
            print(név, file=célfájl)

# 1. feladat
nevek_2011 = fájlból_lista('top100utonev_2011.txt')
nevek_2021 = fájlból_lista('top100utonev_2021.txt')

# 2. feladat
mindkét_évben_szereplő_nevek = []
for név2011 in nevek_2011:
    for név2021 in nevek_2021:
        if név2011['név'] == név2021['név']:
            mindkét_évben_szereplő_nevek.append(név2011['név'])
print(f'Mindkét évben szerepel: {", ".join(mindkét_évben_szereplő_nevek)}, összesen {len(mindkét_évben_szereplő_nevek)} darab.')

# 3. feladat
# Két listát is kell rendeznünk, ezért (is) érdemes rá függvényt írnunk.
# Kérdés, hogy először válogatjuk a neveket nem szerint, és utána rendezünk, 
# vagy fordítva. Mindkét megoldás jó, most mi az utóbbi szerint járunk el.
rendezett_lista = gyakoriság_szerint_rendez(nevek_2021)
#
# Ha a későbbiekben is szeretnénk Python nyelven programozni, mindenképp
# érdemes lesz megismerkedni a sorted() kulcsfüggvényeivel, illetve
# a lambda-függvényekkel. Az alábbi egysoros elvégzi a fenti rendezőfüggvény
# feladatát. A kulcsfüggvény itt annyit mond, hogy "rendezd az elemeket a
# szótárak "szám" kulcsa alapján".
# print(sorted(nevek_2021, key=lambda x: x['szám'], reverse=True))
#
#
# Bonyolultabb, ismétlődő és jól elhatárolható logikai egységet képező 
# feladatunk van, ami függvényért vagy eljárásért kiált.
# Lehetne egy eljárást írnunk, ami nem szerint válogat és a válogatott
# listát fájlba is írja.
# Ha azonban megnézzük a 4. feladatot, látjuk, hogy a nem szerinti válogatásra
# ott is szükség lesz - ezért önálló függvényt kap a nem szerinti válogatás
# és egy önálló eljárást a fájlba írás. 
neveket_fájlba_ír(nem_szerint_válogat(rendezett_lista, 'N'), 'noi_2021.txt')
neveket_fájlba_ír(nem_szerint_válogat(rendezett_lista, 'F'), 'ferfi_2021.txt')

# 4. feladat
női_rendezett_2011 = nem_szerint_válogat(gyakoriság_szerint_rendez(nevek_2011), 'N')
női_rendezett_2021 = nem_szerint_válogat(gyakoriság_szerint_rendez(nevek_2021), 'N')

mindkét_évben = []
for index2011, név in enumerate(női_rendezett_2011):
    if név in női_rendezett_2021: # eldöntés
        index2021 = női_rendezett_2021.index(név) # kiválasztás
        mindkét_évben.append({'név': név, 2011: index2011+1, 2021: index2021+1, 'eltérés': index2011-index2021})
with open('noinevekmozgasa.txt', 'w', encoding='utf-8') as célfájl:
    for bejegyzés in mindkét_évben:
        print(f'{bejegyzés["név"]}\t{bejegyzés[2011]}\t{bejegyzés[2021]}\t{bejegyzés["eltérés"]}', file=célfájl)




