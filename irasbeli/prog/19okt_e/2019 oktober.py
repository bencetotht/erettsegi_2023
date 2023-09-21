"""
2019. október - eUtazás
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2019osz_emelt/e_inf_19okt_fl.pdf
"""
utazasok = []
utazas = {}
with open('utasadat.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        utazas['megallo'] = int(adatok[0])
        dat_ip = adatok[1].split('-')
        utazas['datum'] = dat_ip[0]
        utazas['idopont'] = dat_ip[1]
        utazas['azonosito'] = adatok[2]
        utazas['tipus'] = adatok[3]
        utazas['ervenyes'] = adatok[4]
        utazasok.append(utazas)
        utazas = {}
print(utazasok)


print('2. feladat')
print(f'A buszra {len(utazasok)} utas akart felszállni.')


print('3. feladat')
szamlalo = 0
for utazas in utazasok:
    if (utazas['tipus'] != 'JGY' and utazas['datum'] > utazas['ervenyes']) or \
            (utazas['tipus'] == 'JGY' and utazas['ervenyes'] == '0'):
        szamlalo += 1
print(f'A buszra {szamlalo} utas nem szállhatott fel.')


print('4. feladat')
megallok = []
for index in range(0, 30):
    megallok.append(0)
# a tomb feltöltését nullákkal így is lehetne pythonosan:
# megallok = [0] * 10
for utazas in utazasok:
    megallok[utazas['megallo']] += 1
max_utas = max(megallok)
meg_nem = True
for index, utasok in enumerate(megallok):
    if meg_nem and utasok == max_utas:  # vagy így: utasok == max(megallok)
        print(f'A legtöbb utas ({max_utas} fő) a {index}. megállóban próbált felszállni. ')
        meg_nem = False


print('5. feladat')
ingyenes = 0
kedvezmenyes = 0
for utazas in utazasok:
    if utazas['tipus'] != 'JGY' and utazas['datum'] <= utazas['ervenyes']:
        if utazas['tipus'] == 'NYP' or utazas['tipus'] == 'RVS' or utazas['tipus'] == 'GYK':
            ingyenes += 1
        if utazas['tipus'] == 'TAB' or utazas['tipus'] == 'NYB':
            kedvezmenyes += 1
print(f'Ingyenesen utazók száma: {ingyenes} fő')
print(f'A kedvezményesen utazók száma: {kedvezmenyes} fő')


print('6. feladat')


def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 % 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2 - d1


print('7. feladat')
with open('figyelmeztetes.txt', 'w', encoding='utf-8') as figy:
    for utazas in utazasok:
        if utazas['tipus'] != 'JGY':
            kulonbseg = napokszama(int(utazas['datum'][:4]), int(utazas['datum'][4:6]), int(utazas['datum'][6:]),
                                   int(utazas['ervenyes'][:4]), int(utazas['ervenyes'][4:6]), int(utazas['ervenyes'][6:]),)
            if 0 < kulonbseg < 4:
                print(utazas['azonosito'], utazas['ervenyes'][:4] + '-' + utazas['ervenyes'][4:6] + '-'
                      + utazas['ervenyes'][6:], file=figy)


