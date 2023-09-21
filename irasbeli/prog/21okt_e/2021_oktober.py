"""
2021. október - Sudoku
Javasolt megoldás (A hivatalos megoldás kissé átalakított verziója.)
Feladatlap: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2021osz_emelt/e_inf_21okt_fl.pdf
"""
print('1. feladat')
fajlnev = input('Adja meg a bementi fájl nevét! ')
sor = int(input('Adja meg egy sor számát! ')) - 1
oszlop = int(input('Adja meg egy oszlop számát! ')) - 1

# 2. feladat
tablazat = []
lepesek = []
with open(fajlnev, 'r') as fajl:
    for adtsor in fajl:
        adatsor = adtsor.strip().split()
        ertekek = [int(adat) for adat in adatsor]
        if len(ertekek) == 9:
            tablazat.append(ertekek)
        else:
            lepesek.append(ertekek)

print('3. feladat')
# Lehetne így is:
# if not tablazat[sor][oszlop]:
if tablazat[sor][oszlop] == 0:
    print('Az adott helyet még nem töltötték ki.')
else:
    print(f'Az adott helyen szereplő szám: {tablazat[sor][oszlop]}')
print(f'A hely a(z) {3 * (sor // 3) + (oszlop // 3) + 1} résztáblához tartozik.')

print('4. feladat')
ures_helyek = 0
for s in tablazat:
    for ertek in s:
        if not ertek:
            ures_helyek += 1
print(f'Az üres helyek aránya: {ures_helyek / 81 * 100:.1f}%')

print('5. feladat')
for lepes in lepesek:
    szerepel = False
    szam = lepes[0]
    sor = lepes[1] - 1
    oszlop = lepes[2] - 1
    print(f'A kiválasztott sor: {lepes[1]} oszlop: {lepes[2]} a szám: {lepes[0]}')

    if tablazat[sor][oszlop]:
        print('A helyet már kitöltötték.')
    else:
        if szam in tablazat[sor]:
            print('Az adott sorban már szerepel a szám.')
        else:
            # Lehetne így is:
            # for s in tablazat
            #   if s[oszlop] == szam
            for s in range(9):
                if tablazat[s][oszlop] == szam:
                    szerepel = True
                    break
            if szerepel:
                print('Az adott oszlopban már szerepel a szám.')
            else:
                for s in range(3 * (sor // 3), 3 * (sor // 3) + 3):
                    for o in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                        if tablazat[s][o] == szam:
                            szerepel = True
                if szerepel:
                    print('A résztáblázatban már szerepel a szám.')
                else:
                    print('A lépés megtehető.')















