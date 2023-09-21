"""
Hivatalos mintamegoldás (2021. 10. 27-i állapot)
forrás: https://www.oktatas.hu/kozneveles/erettsegi/feladatsorok/emelt_szint_2021osz/emelt_8nap
"""

print("1. feladat")
fájlnév = input("Adja meg a bemeneti fájl nevét! ")
sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))

# 2. feladat
bemenet = open(fájlnév, "r")
táblázat = []
for i in range(9):
    adatsor = bemenet.readline().strip().split()
    adatok = [int(elem) for elem in adatsor]
    táblázat.append(adatok)
lépés = []
for adatsor in bemenet:
    adatok = [int(elem) for elem in adatsor.strip().split()]
    lépés.append(adatok)

print("3. feladat")
if táblázat[sor - 1][oszlop - 1] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print("Az adott helyen szereplő szám:", táblázat[sor - 1][oszlop - 1])
print("A hely a", 3 * ((sor - 1) // 3) + ((oszlop - 1) // 3) + 1, "résztáblázathoz tartozik.")

print("4. feladat")
üreshely = 0
for sor in táblázat:
    for elem in sor:
        if elem == 0:
            üreshely += 1
print("Az üres helyek aránya: {0:4.1f}%".format(100 * üreshely / 81))

print("5. feladat")
for egylépés in lépés:
    sor = egylépés[1] - 1
    oszlop = egylépés[2] - 1
    szám = egylépés[0]

    print("A kiválasztott sor:", egylépés[1], "oszlop:", egylépés[2], "a szám:", szám)
    if táblázat[sor][oszlop] > 0:
        print("A helyet már kitöltötték.")
    else:
        volt = False
        for o in range(9):
            if táblázat[sor][o] == szám:
                volt = True
        if volt:
            print("Az adott sorban már szerepel a szám.")
        else:
            volt = False
            for s in range(9):
                if táblázat[s][oszlop] == szám:
                    volt = True
            if volt:
                print("Az adott oszlopban már szerepel a szám.")
            else:
                volt = False
                for s in range(3 * (sor // 3), 3 * (sor // 3) + 3):
                    for o in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                        if táblázat[s][o] == szám:
                            volt = True
                if volt:
                    print("A résztáblázatban már szerepel a szám.")
                else:
                    print("A lépés megtehető.")
