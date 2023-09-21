"""
2020. május (idegen nyelvű) - Menetrend
strukturáltabb adatszerkezet -> egyszerűbb megoldás a 7. feladatnál
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2020tavasz_emelt/e_infma_20maj_fl.pdf
"""
# menetrend = {
#     1: {
#         0: {
#             'indulas': 345
#         },
#         1: {
#             'erkezes': 360
#             'indulas': 362
#         },
#         2: {
#             'erkezes': 372
#             'indulas': 373
#         }
#         ...allomas...
#     ...vonat...
#     }
# }

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

print(menetrend)


print('2. feladat')
print(f'Az állomások száma: {len(menetrend[1])}')
print(f'A vonatok száma: {len(menetrend)}')


print('3. feladat')
maxx = {'allasido': menetrend[1][1]['indulas'] - menetrend[1][1]['erkezes'], 'vonat': 1, 'allomas': 1}
for vonat in menetrend:
    for allomas in range(1, len(menetrend[vonat]) - 1):
        if menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes'] > maxx['allasido']:
            maxx['allasido'] = menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes']
            maxx['vonat'] = vonat
            maxx['allomas'] = allomas
print(f"A(z) {maxx['vonat']}. vonat a(z) {maxx['allomas']}. állomáson {maxx['allasido']} percet állt.")


print('4. feladat')
vizsgalt_vonat = 2 # int(input('Adja meg egy vonat azonosítóját!'))
ora_perc = '7 16' # input('Adjon meg egy időpontot (óra perc)!')


print('5. feladat')
eloirt = 2 * 60 + 22
elteres = eloirt - (menetrend[vizsgalt_vonat][len(menetrend[vizsgalt_vonat])-1]['erkezes'] - menetrend[vizsgalt_vonat][0]['indulas'])
if elteres < 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel rövidebb volt az előírtnál.')
elif elteres == 0:
    print(f'A(z) {vizsgalt_vonat}. vonat útja pontosan az előírt ideig tartott.')
else:
    print(f'A(z) {vizsgalt_vonat}. vonat útja {abs(elteres)} perccel hosszabb volt az előírtnál.')


# print('6. feladat')
def valto(m):
    return str(m // 60) + ':' + str(m % 60)


fajlnev = 'halad' + str(vizsgalt_vonat) + '.txt'
with open(fajlnev, 'w', encoding='utf-8') as halad:
    for allomas in range(1, len(menetrend[vizsgalt_vonat])):
        print(f"{allomas}. állomás {valto(menetrend[vizsgalt_vonat][allomas]['erkezes'])}", file=halad)


print('7. feladat')
idopont = int(ora_perc.split()[0]) * 60 + int(ora_perc.split()[1])
for vonat in menetrend:
    if menetrend[vonat][0]['indulas'] < idopont < menetrend[vonat][1]['erkezes']:
        print(f"A(z) {vonat}. vonat a 0. és a 1. állomás között járt. ")
    for allomas in range(1, len(menetrend[vonat])-1):
        if menetrend[vonat][allomas]['erkezes'] <= idopont <= menetrend[vonat][allomas]['indulas']:
            print(f"A(z) {vonat}. vonat a {allomas}. állomáson állt.")
        if menetrend[vonat][allomas]['indulas'] < idopont < menetrend[vonat][allomas + 1]['erkezes']:
            print(f"A(z) {vonat}. vonat a {allomas}. és a {allomas + 1}. állomás között járt. ")
