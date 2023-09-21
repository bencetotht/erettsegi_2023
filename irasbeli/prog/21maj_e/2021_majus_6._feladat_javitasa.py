"""
2021. május - Gödrök
A 2021. májusi informatika érettségi programozási feladatához készült - az alábbi linken közzétett -
hivatalos mintamegoldás a 6. részfeladatban a 2021.05.19-i állapot szerint több hibát is tartalmaz.

Az alábbi kód ezen hibák javítását tartalmazza az eredeti logika és változónevek megtartásával.

Feladatlap:
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2021tavasz_emelt/e_inf_21maj_fl.pdf
Hivatalos mintamegoldás:
https://www.oktatas.hu/bin/content/dload/erettsegi/feladatok_2021tavasz_emelt/e_infmeg_21maj_ut.zip
"""

# Forrásfájl adatainak beolvasása
bemenet = open("melyseg.txt")
mélységek = []
for sor in bemenet:
    mélységek.append(int(sor.strip()))


# Ebben a feladatban adja meg a felhasználó a 6. feldathoz szükséges adatot.
print("2. feladat")
hely = int(input("Adjon meg egy távolságértéket! "))
print(f'Ezen a helyen a felszín {mélységek[hely - 1]} méter mélyen van.')


# A javított részfeladat:
print("6. feladat")
if mélységek[hely - 1] > 0:
    print("a)")
    poz = hely - 1
    while mélységek[poz] > 0:
        poz -= 1
    kezdő = poz + 2
    poz = hely - 1
    while mélységek[poz] > 0:
        poz += 1
    záró = poz
    print(f'A gödör kezdete: {kezdő} méter, a gödör vége: {záró} méter.')

    print("b)")
    mélypont = 0
    poz = kezdő
    while mélységek[poz] >= mélységek[poz - 1] and poz <= záró - 1:
        poz += 1
    while mélységek[poz] <= mélységek[poz - 1] and poz <= záró - 1:
        poz += 1
    if poz == záró:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    print("c)")
    print(f'A legnagyobb mélysége {max(mélységek[kezdő - 1:záró])} méter.')

    print("d)")
    térfogat = 10 * sum(mélységek[kezdő - 1:záró])
    print(f'A térfogata {térfogat} m^3.')

    print("e)")
    biztonságos = térfogat - 10 * (záró - kezdő + 1)
    print(f'A vízmennyiség {biztonságos} m^3.')

else:
    print("Az adott helyen nincs gödör.")




# Hibákat tartalamazó kódrészlet  a hivatalos mintamegoldásból (2021.05.19-i állapot):
# print("6. feladat")
# if mélységek[hely] > 0:
#     print("a)")
#     poz=hely
#     while mélységek[poz] > 0:
#         poz -= 1
#     kezdő = poz+2
#     poz = hely
#     while mélységek[poz] > 0:
#         poz += 1
#     záró = poz
#     print(f'A gödör kezdete: {kezdő} méter, a gödör vége: {záró} méter.')
#
#     print("b)")
#     mélypont = 0
#     poz = kezdő+1
#     while mélységek[poz] <= mélységek[poz-1] and poz <= záró:
#         poz += 1
#     while mélységek[poz] >= mélységek[poz-1] and poz <= záró:
#         poz += 1
#     if poz > záró:
#         print("Folyamatosan mélyül.")
#     else:
#         print("Nem mélyül folyamatosan.")
#
#     print("c)")
#     print(f'A legnagyobb mélysége {max(mélységek[kezdő-1:záró])} méter.')
#
#     print("d)")
#     térfogat=10*sum(mélységek[kezdő-1:záró])
#     print(f'A térfogata {térfogat} m^3.')
#
#     print("e)")
#     biztonságos=térfogat-10*(záró-kezdő+1)
#     print(f'A vízmennyiség {biztonságos} m^3.')
# else:
#     print("Az adott helyen nincs gödör.")
