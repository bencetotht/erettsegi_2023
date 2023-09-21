"""
2019. május (idegen nyelvű) - Tantárgyfelosztás
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2019tavasz_emelt/e_infma_19maj_fl.pdf
"""
tantargyfelosztas = []
ora = {}
adatok = []
with open('beosztas.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok.append(sor.strip())
        if len(adatok) == 4:
            ora['tanar'] = adatok[0]
            ora['tantargy'] = adatok[1]
            ora['osztaly'] = adatok[2]
            ora['oraszam'] = int(adatok[3])
            tantargyfelosztas.append(ora)
            ora = {}
            adatok = []
print(tantargyfelosztas)

print('2. feladat')
print(f'A fájlban {len(tantargyfelosztas)} bejegyzés van')


print('3. feladat')
szamlalo = 0
for ora in tantargyfelosztas:
    szamlalo += ora['oraszam']
print(f'Az iskolában a heti összóraszám: {szamlalo}')


print('4. feladat')
tanar = 'Albatrosz Aladin' # input('Egy tanár neve= ')
szamlalo = 0
for ora in tantargyfelosztas:
    if tanar == ora['tanar']:
        szamlalo += ora['oraszam']
print(f'A tanár heti óraszáma: {szamlalo}')


print('5. feladat')
with open('of.txt', 'w', encoding='utf-8') as of:
    for ora in tantargyfelosztas:
        if ora['tantargy'] == "osztalyfonoki":
            print(f"{ora['osztaly']} - {ora['tanar']}", file=of)


print('6. feladat')
osztaly = '10.b' # input('Osztály= ')
tantargy = 'kemia' # input('Tantargy= ')
szamlalo = 0
for ora in tantargyfelosztas:
    if ora['osztaly'] == osztaly and ora['tantargy'] == tantargy:
        szamlalo += 1
if szamlalo > 1:
    print('Csoportbontásban tanulják.')
else:
    print('Osztályszinten tanulják.')


print('7. feladat')
tanarok = set()
for ora in tantargyfelosztas:
    tanarok.add(ora['tanar'])
print(f'Az iskolában {len(tanarok)} tanár tanít.')