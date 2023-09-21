"""
2017. május (idegen nyelvű) - Fürdő
            Strukturáltabb adatszerkezet -> egyszerűbb algoritmus
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2017tavasz_emelt/e_infma_17maj_fl.pdf
"""
furdo = {}
with open('baddaten.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        ido = int(adatok[3]) * 3600 + int(adatok[4]) * 60 + int(adatok[5])
        if int(adatok[0]) not in furdo:
            furdo[int(adatok[0])] = {}
            furdo[int(adatok[0])][int(adatok[1])] = []
            furdo[int(adatok[0])][int(adatok[1])].append(ido)
        else:
            if int(adatok[1]) not in furdo[int(adatok[0])]:
                furdo[int(adatok[0])][int(adatok[1])] = []
            furdo[int(adatok[0])][int(adatok[1])].append(ido)
print(furdo[145])


def atvalt(sec):
    p, mp = divmod(sec, 60)
    o, p = divmod(p, 60)
    return f"{o}:{p}:{mp}"


print('2. feladat')
meg_nem = True
utolso = None
for vendeg in furdo:
    if meg_nem:
        print(f"Az első vendég {atvalt(furdo[vendeg][0][0])}-kor lépett ki az öltözőből.")
        meg_nem = False
    utolso = furdo[vendeg][0][0]
print(f"Az utolsó vendég {atvalt(utolso)}-kor lépett ki az öltözőből.")


print('3. feladat')
szamlalo = 0
for vendeg in furdo:
    egy_reszleg = True
    if len(furdo[vendeg]) == 2:
        for reszleg in furdo[vendeg]:
            if len(furdo[vendeg][reszleg]) != 2:
                egy_reszleg = False
    else:
        egy_reszleg = False
    if egy_reszleg:
        szamlalo += 1
print(f'A fürdőben {szamlalo} vendég járt csak egy részlegen. ')


print('4. feladat')
max_ido = 0
max_vendeg = 0
for vendeg in furdo:
    if furdo[vendeg][0][1] - furdo[vendeg][0][0] > max_ido:
        max_ido = furdo[vendeg][0][1] - furdo[vendeg][0][0]
        max_vendeg = vendeg
print('A legtöbb időt eltöltő vendég:')
print(f"{max_vendeg}. vendég {atvalt(max_ido)}")


print('5. feladat')
ora6_9 = 0
ora9_16 = 0
ora16_20 = 0
for vendeg in furdo:
    if 6 * 3600 <= furdo[vendeg][0][0] <= 9 * 3600:
        ora6_9 += 1
    elif 9 * 3600 <= furdo[vendeg][0][0] <= 16 * 3600:
        ora9_16 += 1
    else:
        ora16_20 += 1
print(f'6-9 óra között {ora6_9} vendég')
print(f'9-16 óra között {ora9_16} vendég')
print(f'16-20 óra között {ora16_20} vendég')


print('6. feladat')
with open('szauna1.txt', 'w', encoding='utf-8') as szauna:
    for vendeg in furdo:
        szauna_ido = 0
        if 2 in furdo[vendeg]:
            for index in range(0, len(furdo[vendeg][2])-1, 2):
                szauna_ido += furdo[vendeg][2][index+1] - furdo[vendeg][2][index]
            if szauna_ido:
                print(f'{vendeg} {atvalt(szauna_ido)}')


print('7. feladat')
uszoda = 0
szaunak = 0
medencek = 0
strand = 0
for vendeg in furdo:
    if 1 in furdo[vendeg]:
        uszoda += 1
    if 2 in furdo[vendeg]:
        szaunak += 1
    if 3 in furdo[vendeg]:
        medencek += 1
    if 4 in furdo[vendeg]:
        strand += 1
print(f'Uszoda: {uszoda}')
print(f'Szaunák: {szaunak}')
print(f'Gyógyvizes medncék: {medencek}')
print(f'Strand: {strand}')