"""
2020. október - Sorozatok
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2020osz_emelt/e_inf_20okt_fl.pdf
"""

epizod = {}  # egy epizód tárolására
epizodok = []

adatok = []
with open('lista.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok.append(sor.strip())
        if len(adatok) == 5:
            epizod['datum'] = adatok[0]
            epizod['sorozat'] = adatok[1]
            epizod['resz'] = adatok[2]
            epizod['hossz'] = int(adatok[3])
            if adatok[4] == '1':
                epizod['latta'] = True
            else:
                epizod['latta'] = False

            epizodok.append(epizod)
            epizod = {}
            adatok = []
print(epizodok)

print('2. feladat')
szamlalo = 0
for epizod in epizodok:
    if 'NI' not in epizod['datum']:
        szamlalo += 1
print(f'A listában {szamlalo} db vetítési dátummal rendelkező epizód van.')

print('3. feladat')
szamlalo = 0
for epizod in epizodok:
    if epizod['latta']:
        szamlalo += 1
szazalek = szamlalo / len(epizodok) * 100
print(f'A listában lévő epizódok {szazalek:.2f}% -át látta.')

print('4. feladat')
perc_osszesen = 0
for epizod in epizodok:
    if epizod['latta']:
        perc_osszesen += epizod['hossz']
nap = perc_osszesen // (24 * 60)
ora = perc_osszesen % (24 * 60) // 60
perc = perc_osszesen % 60
print(f'Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.')

print('5. feladat')
datum = input('Adjon meg egy dátumot! Dátum= ')
for epizod in epizodok:
    if epizod['datum'] <= datum and not epizod['latta']:
        print(epizod['resz'] + '\t' + epizod['sorozat'])

print('6. feladat')


def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if honap < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev //
                      400 + honapok[honap - 1] + nap) % 7]
    return hetnapja


print('7. feladat')
vizsgalt_nap = input('Adja meg a hét egy napját (például cs)! Nap=')
aznapi_sororozatok = set()
for epizod in epizodok:
    if 'NI' not in epizod['datum']:
        epizod_datuma = epizod['datum'].split('.')
        epizod_napja = hetnapja(int(epizod_datuma[0]), int(epizod_datuma[1]), int(epizod_datuma[2]))
    if vizsgalt_nap == epizod_napja:
        aznapi_sororozatok.add(epizod['sorozat'])
if len(aznapi_sororozatok):
    for elem in aznapi_sororozatok:
        print(elem)
else:
    print('Az adott napon nem kerül adásba sorozat.')

# sorozatok = {
#   'Games': {
#       'darab_resz': 7,
#       'ossz_hossz': 420
#       },
#    ...
#  }
print('8. feladat')
sorozatok = {}
for epizod in epizodok:
    if sorozatok.get(epizod['sorozat'], 0):
        sorozatok[epizod['sorozat']]['darab_resz'] += 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] += epizod['hossz']
    else:
        sorozatok[epizod['sorozat']] = {}
        sorozatok[epizod['sorozat']]['darab_resz'] = 1
        sorozatok[epizod['sorozat']]['ossz_hossz'] = epizod['hossz']
with open('summa.txt', 'w', encoding='utf-8') as summa:
    for kulcs in sorozatok:
        print(kulcs, sorozatok[kulcs]['ossz_hossz'], sorozatok[kulcs]['darab_resz'], file=summa)
