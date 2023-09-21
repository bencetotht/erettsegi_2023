"""
2021. május idegen nyelvű - Bányató
https://sulipy.hu/erettsegi
https://www.oktatas.hu/bin/content/dload/erettsegi/feladatok_2021tavasz_emelt/e_infma_21maj_fl.pdf
"""
melysegek = []
with open('melyseg.txt', 'r') as fajl:
    for index, egy_sor in enumerate(fajl):
        if index > 1:
            sor = []
            sor = list(map(int, egy_sor.strip().split()))
            melysegek.append(sor)
# print(melysegek)

print('2. feladat')
sor = int(input('A mérés sorának azonosítója = '))
oszlop = int(input('A mérés oszlopának azonosítója = '))
print(f'A mért mélység az adott helyen {melysegek[sor - 1][oszlop - 1]} dm')


print('3. feladat')
szamlalo = 0
melyseg_osszesen = 0
for sor in melysegek:
    melyseg_osszesen += sum(sor)
    for melyseg in sor:
        if melyseg > 0:
            szamlalo += 1
print(f'A tó felszíne: {szamlalo} m2, átlagos mélysége: {melyseg_osszesen / szamlalo / 10:.2f} m')


print('4. feladat')
max_melyseg = 0
for sor in melysegek:
    if max(sor) > max_melyseg:
        max_melyseg = max(sor)
print(f'A tó legnagyobb mélysége: {max_melyseg} dm')
print('A legmélyebb helyek sor-oszlop koordinátái:')
for i, sor in enumerate(melysegek):
    for j, melyseg in enumerate(sor):
        if melysegek[i][j] == max_melyseg:
            print(f'({i+1}; {j+1})', end='\t')


print('5. feladat')
hossz = 0
for i, sor in enumerate(melysegek):
    for j, melyseg in enumerate(sor):
        if melyseg > 0:
            if j > 0 and sor[j-1] == 0:
                hossz += 1
            if j < len(sor) - 1 and sor[j+1] == 0:
                hossz += 1
            if i > 0 and melysegek[i-1][j] == 0:
                hossz += 1
            if i < len(melysegek) - 1 and melysegek[i+1][j] == 0:
                hossz += 1
print(f'A tó partvonala {hossz} m hosszú')
# Ennél a feladatnál feleslegesen túlbiztosítottam a dolgokat a videóban. Mivel feladat megadja, 
# hogy a legszélső sorokban és oszlopokban lévő cellák értéke mindíg nulla, az alul- és túlindexelésre nem kell figyelni,
# ezért a fenti kód így egyszerűsödhetne:
# print('5. feladat')
# hossz = 0
# for i, sor in enumerate(melysegek):
#    for j, melyseg in enumerate(sor):
#        if melyseg > 0:
#            if sor[j-1] == 0:
#                hossz += 1
#            if sor[j+1] == 0:
#                hossz += 1
#            if melysegek[i-1][j] == 0:
#                hossz += 1
#            if melysegek[i+1][j] == 0:
#                hossz += 1
# print(f'A tó partvonala {hossz} m hosszú')




print('6. feladat')
oszlop = int(input('A vizsgált szelvény oszlopának azonosítója = '))
with open('diagram.txt', 'w') as diagram:
    for index, sor in enumerate(melysegek):
        # print(sor[oszlop-1])
        print(f'{index+1:02d}', '*' * round(sor[oszlop-1] / 10), file=diagram)



























