"""
2019. május - Céges autók
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2019tavasz_emelt/e_inf_19maj_fl.pdf
"""
athaladasok = []
athaladas = {}

with open('autok.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        athaladas['nap'] = int(adatok[0])
        athaladas['idopont'] = adatok[1]
        athaladas['rendszam'] = adatok[2]
        athaladas['szemely'] = adatok[3]
        athaladas['km'] = int(adatok[4])
        if adatok[5] == '0':
            athaladas['ki'] = True
        else:
            athaladas['ki'] = False
        athaladasok.append(athaladas)
        athaladas = {}

print(athaladasok)


print('2. feladat')
utolso_auto = 0
for index, athaladas in enumerate(athaladasok):
    if athaladas['ki']:
        utolso_auto = index
print(f"{athaladasok[utolso_auto]['nap']} nap rendszám: {athaladasok[utolso_auto]['rendszam']}")


print('3. feladat')
nap = int(input('Nap: '))
print(f'Forgalom a(z) {nap}. napon:')
for athaladas in athaladasok:
    if athaladas['nap'] == nap:
        irany = 'ki' if athaladas['ki'] else 'be'
        print(f"{athaladas['idopont']} {athaladas['rendszam']} {athaladas['szemely']} {irany}")


print('4. feladat')
kint_van = set()
for athaladas in athaladasok:
    if athaladas['ki']:
        kint_van.add(athaladas['rendszam'])
    else:
        kint_van.remove(athaladas['rendszam'])
print(f'A hónap végén {len(kint_van)} autót nem hoztak vissza.')


# Beágyazott szótárral való megoldás
# megtett_km = {
#       'rendszam': {
#           'kezdo km': km
#           'aktualis km': km
#       },
#        ...
#   }
print('5. feladat')
megtett_km = {}
for athaladas in athaladasok:
    if megtett_km.get(athaladas['rendszam'], 0):
        megtett_km[athaladas['rendszam']]['aktualis km'] = athaladas['km']
    else:
        megtett_km[athaladas['rendszam']] = {}
        megtett_km[athaladas['rendszam']]['kezdo km'] = athaladas['km']
        megtett_km[athaladas['rendszam']]['aktualis km'] = athaladas['km']
print(megtett_km)
for rendszam in megtett_km:
    print(rendszam, megtett_km[rendszam]['aktualis km'] - megtett_km[rendszam]['kezdo km'])


# Beágyazott szótár nélküli megoldás
# megtett_km = {
#       'rendszam': [kezdo_km, aktualis_km],
#        ...
#   }
print('5. feladat')
megtett_km = {}
for athaladas in athaladasok:
    if megtett_km.get(athaladas['rendszam'], 0):
        megtett_km[athaladas['rendszam']][1] = athaladas['km']
    else:
        megtett_km[athaladas['rendszam']] = {}
        megtett_km[athaladas['rendszam']] = [athaladas['km'], athaladas['km']]
print(megtett_km)
for rendszam in megtett_km:
    print(rendszam, megtett_km[rendszam][1] - megtett_km[rendszam][0])


print('6. feladat')
max_szemely = None
max_km = 0
for index, athaladas in enumerate(athaladasok):
    if not athaladas['ki']:
        vissza_index = index - 1
        while athaladas['rendszam'] != athaladasok[vissza_index]['rendszam']:
            if vissza_index >= 0:
                vissza_index -= 1
        if athaladas['km'] - athaladasok[vissza_index]['km'] > max_km:
            max_km = athaladas['km'] - athaladasok[vissza_index]['km']
            max_szemely = athaladas['szemely']
print(f'Leghosszabb út: {max_km} km, személy: {max_szemely}')


print('7. feladat')
rendszam = input('Rendszam: ')
fajlnev = rendszam + '_mentlevel.txt'
with open(fajlnev, 'w', encoding='utf-8') as menetlevel:
    for athaladas in athaladasok:
        if athaladas['rendszam'] == rendszam:
            if athaladas['ki']:
                print(athaladas['szemely'] + '\t' + str(athaladas['nap']) + '.\t' + athaladas['idopont'] + '\t' \
                           + str(athaladas['km']) + ' km\t', end='', file=menetlevel)
            if not athaladas['ki']:
                print(str(athaladas['nap']) + '.\t' + athaladas['idopont'] + '\t' \
                           + str(athaladas['km']) + ' km\t', file=menetlevel)
print('Menetlevél kész.')

