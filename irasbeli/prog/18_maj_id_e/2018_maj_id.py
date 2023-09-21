"""
2018. május (idegen nyelvű) - Fogadóóra
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2018tavasz_emelt/e_infma_18maj_fl.pdf
"""
megbeszelesek = []
megbeszeles = {}
with open('fogado.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        foglalas = adatok[3].split('-')
        megbeszeles['tanar'] = adatok[0] + ' ' + adatok[1]
        megbeszeles['idopont'] = adatok[2]
        megbeszeles['f_datum'] = foglalas[0]
        megbeszeles['f_idopont'] = foglalas[1]
        megbeszelesek.append(megbeszeles)
        megbeszeles = {}
print(megbeszelesek)

print('2. feladat')
print(f'Foglalások száma: {len(megbeszelesek)}')


print('3. feladat')
nev = 'Nagy Ferenc' # input('Adjon meg egy nevet: ')
szamlalo = 0
for megbeszeles in megbeszelesek:
    if megbeszeles['tanar'] == nev:
        szamlalo += 1
print(f'{nev} néven {szamlalo} időpontfoglalás van.')


print('4. feladat')
idopont = '17:40' # input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
tanarok = []
for megbeszeles in megbeszelesek:
    if idopont == megbeszeles['idopont']:
        tanarok.append(megbeszeles['tanar'])
tanarok.sort()
fajl_nev = idopont[:2] + idopont[3:] + '.txt'
with open(fajl_nev, 'w', encoding='utf-8') as kimenet:
    for tanar in tanarok:
        print(tanar)
        print(tanar, file=kimenet)


print('5. feladat')
min_idopont = megbeszelesek[0]['f_datum'] + '-' + megbeszelesek[0]['f_idopont']
min_index = 0
for index, megbeszeles in enumerate(megbeszelesek):
    if megbeszeles['f_datum'] + '-' + megbeszeles['f_idopont'] < min_idopont:
        min_idopont = megbeszeles['f_datum'] + megbeszeles['f_idopont']
        min_index = index
print(f"Tanár neve: {megbeszelesek[min_index]['tanar']}")
print(f"Foglalt időpont: {megbeszelesek[min_index]['idopont']}")
print(f'Foglalás ideje: {min_idopont}')


print('6. feladat')
idopontok = {}
for o in range(6, 8):
    for p in range(0, 6):
        idopont = '1' + str(o) + ':' + str(p) + '0'
        idopontok[idopont] = False
for megbeszeles in megbeszelesek:
    if megbeszeles['tanar'] == 'Barna Eszter':
        idopontok[megbeszeles['idopont']] = True
print(idopontok)
utolso = None
for ip, foglalt in idopontok.items():
    if not foglalt:
        print(ip)
    if foglalt:
        utolso = ip
idopontok_listaja = list(idopontok.keys())
utolso_index = idopontok_listaja.index(utolso)
if utolso_index < len(idopontok_listaja) - 1:
    print(f'Barna Eszter legkorábban távozhat: {idopontok_listaja[utolso_index + 1]}')
else:
    print(f'Barna Eszter legkorábban távozhat: 18:00')


