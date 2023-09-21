"""
2017. május (idegen nyelvű) - Fürdő
            Egyszerű adatszerkezet -> bonyolultabb algoritmus
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2017tavasz_emelt/e_infma_17maj_fl.pdf
"""
bejegyzes = {}
furdo = []
with open('baddaten.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        bejegyzes['vendeg'] = adatok[0]
        bejegyzes['reszleg'] = adatok[1]
        bejegyzes['be'] = True if adatok[2] == '0' else False
        bejegyzes['ido'] = int(adatok[3]) * 3600 + int(adatok[4]) * 60 + int(adatok[5])
        furdo.append(bejegyzes)
        bejegyzes = {}
print(furdo)


def atvalt(sec):
    p, mp = divmod(sec, 60)
    o, p = divmod(p, 60)
    return f"{o}:{p}:{mp}"


print('2. feladat')
meg_nem = True
utolso = None
for bejegyzes in furdo:
    if meg_nem and bejegyzes['reszleg'] == '0' and not bejegyzes['be']:
        print(f"Az első vendég {atvalt(bejegyzes['ido'])}-kor lépett ki az öltözőből.")
        meg_nem = False
    if bejegyzes['reszleg'] == '0' and not bejegyzes['be']:
        utolso = bejegyzes['ido']
print(f"Az utolsó vendég {atvalt(utolso)}-kor lépett ki az öltözőből.")


print('3. feladat')
reszlegek = 0
egy_reszlegesek = 0
for index in range(len(furdo) - 2):
    if furdo[index]['vendeg'] == furdo[index + 1]['vendeg']:
        # print(furdo[index]['reszleg'], end='')
        reszlegek += 1
    else:
        # print(furdo[index]['reszleg'])
        reszlegek += 1
        if reszlegek == 4:
            egy_reszlegesek += 1
        reszlegek = 0
print(f'A fürdőben {egy_reszlegesek} vendég járt csak egy részlegen. ')


print('4. feladat')
max_ido = 0
max_index = 0
for index, bejegyzes in enumerate(furdo):
    if bejegyzes['reszleg'] == '0' and bejegyzes['be']:
        vissza_index = index - 1
        while bejegyzes['vendeg'] != furdo[vissza_index]['vendeg'] or furdo[vissza_index]['reszleg'] != '0':
            vissza_index -= 1
        if bejegyzes['ido'] - furdo[vissza_index]['ido'] > max_ido:
            max_ido = bejegyzes['ido'] - furdo[vissza_index]['ido']
            max_index = index
print('A legtöbb időt eltöltő vendég:')
print(f"{furdo[max_index]['vendeg']}. vendég {atvalt(max_ido)}")


print('5. feladat')
ora6_9 = 0
ora9_16 = 0
ora16_20 = 0
for bejegyzes in furdo:
    if bejegyzes['reszleg'] == '0' and not bejegyzes['be']:
        if 6 * 3600 <= bejegyzes['ido'] <= 9 * 3600:
            ora6_9 += 1
        elif 9 * 3600 <= bejegyzes['ido'] <= 16 * 3600:
            ora9_16 += 1
        else:
            ora16_20 += 1
print(f'6-9 óra között {ora6_9} vendég')
print(f'9-16 óra között {ora9_16} vendég')
print(f'16-20 óra között {ora16_20} vendég')


print('6. feladat')
with open('szauna.txt', 'w', encoding='utf-8') as szauna:
    szauna_ido = 0
    for index in range(len(furdo) - 2):
        if furdo[index]['vendeg'] == furdo[index + 1]['vendeg']:
            if furdo[index]['reszleg'] == '2' and furdo[index]['be']:
                print(furdo[index])
                print(furdo[index+1])
                szauna_ido += furdo[index + 1]['ido'] - furdo[index]['ido']
        else:
            if szauna_ido:
                print(f"{furdo[index]['vendeg']} {atvalt(szauna_ido)}", file=szauna)
            szauna_ido = 0


print('7. feladat')
uszoda = set()
szaunak = set()
medencek = set()
strand = set()
for bejegyzes in furdo:
    if bejegyzes['reszleg'] == '1':
        uszoda.add(bejegyzes['vendeg'])
    elif bejegyzes['reszleg'] == '2':
        szaunak.add(bejegyzes['vendeg'])
    elif bejegyzes['reszleg'] == '3':
        medencek.add(bejegyzes['vendeg'])
    elif bejegyzes['reszleg'] == '4':
        strand.add(bejegyzes['vendeg'])
print(f'Uszoda: {len(uszoda)}')
print(f'Szaunák: {len(szaunak)}')
print(f'Gyógyvizes medncék: {len(medencek)}')
print(f'Strand: {len(strand)}')