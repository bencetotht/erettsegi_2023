"""
2020. május (idegen nyelvű) - Menetrend
egyszerűbb adatszerkezet -> bonyolultabb megoldása  7. feladatnál
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2020tavasz_emelt/e_infma_20maj_fl.pdf
"""
athaladas = {}
athaladasok = []
with open('vonat.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        athaladas['vonat'] = int(adatok[0])
        athaladas['allomas'] = int(adatok[1])
        athaladas['ora'] = int(adatok[2])
        athaladas['perc'] = int(adatok[3])
        athaladas['ido_percben'] = int(adatok[2]) * 60 + int(adatok[3])
        athaladas['indul'] = True if adatok[4] == 'I' else False
        athaladasok.append(athaladas)
        athaladas = {}
print(athaladasok)

print('2. feladat')
allomasok = set()
vonatok = set()
for athaladas in athaladasok:
    allomasok.add(athaladas['allomas'])
    vonatok.add(athaladas['vonat'])
print(f'Az állomások száma: {len(allomasok)}')
print(f'A vonatok száma: {len(vonatok)}')


print('3. feladat')
max_allas_ido = 0
max_athaladas = {}
for index, athaladas in enumerate(athaladasok):
    if athaladas['indul'] and athaladas['allomas']:
        vissza_index = index - 1
        while athaladas['vonat'] != athaladasok[vissza_index]['vonat']:
            vissza_index -= 1
        allas_ido = athaladas['ido_percben'] - athaladasok[vissza_index]['ido_percben']
        if allas_ido > max_allas_ido:
            max_allas_ido = allas_ido
            max_athaladas = athaladas
print(f"A(z) {max_athaladas['vonat']}. vonat a(z) {max_athaladas['allomas']}. állomáson {max_allas_ido} percet állt.")


print('4. feladat')
vizsgalt_vonat = 2 # int(input('Adja meg egy vonat azonosítóját!'))
ora_perc = '7 16' # input('Adjon meg egy időpontot (óra perc)!')

print('5. feladat')
eloirt = 2 * 60 + 22
vizsgalt_indulas = 0
vizsgalt_erkezes = 0
for athaladas in athaladasok:
    if athaladas['allomas'] == 0 and athaladas['vonat'] == vizsgalt_vonat:
        vizsgalt_indulas = athaladas['ido_percben']
    if athaladas['allomas'] == len(allomasok) - 1 and athaladas['vonat'] == vizsgalt_vonat:
        vizsgalt_erkezes = athaladas['ido_percben']
elteres = eloirt - (vizsgalt_erkezes - vizsgalt_indulas)
if elteres < 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel rövidebb volt az előírtnál.')
elif elteres == 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja pontosan az előírt ideig tartott.')
else:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel hosszabb volt az előírtnál.')


print('6. feladat')
fajlnev = 'halad' + str(vizsgalt_vonat) + '.txt'
with open(fajlnev, 'w', encoding='utf-8') as halad:
    for athaladas in athaladasok:
        if athaladas['vonat'] == vizsgalt_vonat and not athaladas['indul']:
            print(f"{athaladas['allomas']}. állomás {athaladas['ora']}:{athaladas['perc']}", file=halad)


print('7. feladat')
print(ora_perc)
vege = False
idopont = int(ora_perc.split()[0]) * 60 + int(ora_perc.split()[1])
for vonat in range(1, len(vonatok)+1):
    if vege:
        break
    for index, athaladas in enumerate(athaladasok):
        if vonat == athaladas['vonat']:
            if idopont == athaladas['ido_percben'] and athaladas['allomas'] != 0 and athaladas['allomas'] != len(allomasok)-1:
                print(f"A {athaladas['vonat']}. vonat {athaladas['allomas']}. állomáson állt.")
                break
            if idopont < athaladas['ido_percben'] and athaladas['allomas'] != 0:
                if athaladas['indul']:
                    print(f"A {athaladas['vonat']}. vonat {athaladas['allomas']}. állomáson állt.")
                    break
                else:
                    print(f"A {athaladas['vonat']}. vonat {athaladas['allomas'] - 1}. és az {athaladas['allomas']}. állomás között volt.")
                    break
            if idopont <= athaladas['ido_percben'] and athaladas['allomas'] == 0:
                vege = True
                break

print('---------------------')
menetrend = {}
with open('vonat.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        for index, item in enumerate(adatok):
            if index != 4:
                adatok[index] = int(item)

        if adatok[0] not in menetrend:
            menetrend[adatok[0]] = {}
        if adatok[1] not in menetrend[adatok[0]]:
            menetrend[adatok[0]][adatok[1]] = {}
        if adatok[4] == 'I':
            menetrend[adatok[0]][adatok[1]]['indulas'] = adatok[2] * 60 + adatok[3]
        else:
            menetrend[adatok[0]][adatok[1]]['erkezes'] = adatok[2] * 60 + adatok[3]

print(menetrend[5])

# def ora(m):
#     return str(m // 60) + ' ' + str(m % 60)

for vonat in menetrend:
    if menetrend[vonat][0]['indulas'] < idopont < menetrend[vonat][1]['erkezes']:
        print(f"A(z) {vonat}. vonat a 0. és a 1. állomás között járt. ")
    for allomas in range(1, len(allomasok) - 1):
        if menetrend[vonat][allomas]['erkezes'] <= idopont <= menetrend[vonat][allomas]['indulas']:
            print(f"A(z) {vonat}. vonat a {allomas}. állomáson állt.")
        if menetrend[vonat][allomas]['indulas'] < idopont < menetrend[vonat][allomas + 1]['erkezes']:
            print(f"A(z) {vonat}. vonat a {allomas}. és a {allomas + 1}. állomás között járt. ")

