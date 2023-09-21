hianyzasok = []
mennyiseg = 0
with open('naplo.txt', 'r', encoding='utf8') as f:
    datum = ''
    napi_hianyzas = []
    for line in f.readlines():
        sor = line.strip().split()
        if sor[0] == "#": 
            datum = f'{sor[1]}-{sor[2]}'
        else:
            mennyiseg += 1
            hianyzasok.append({'datum': datum,'nev': f'{sor[0]} {sor[1]}', 'hianyzasok': sor[2]})

print(f'2. feladat\nA naplóban {mennyiseg} hiányzás van.')
igazolt = 0
igazolatlan = 0
for hianyzas in hianyzasok:
    for letter in hianyzas['hianyzasok']:
        if letter == "X": igazolt += 1
        elif letter == "I": igazolatlan += 1

print(f'\n3.feladat\nAz igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

# user_month = int(input('\n5.feladat\nA hónap sorszáma= '))
# user_day = int(input('A nap sorszáma= '))
# print(f'Azon a napon {hetnapja(user_month, user_day)} volt.')

# user_weekday = input('\n6.feladat\nA nap neve= ')
# user_num = int(input('Az óra sorszáma= '))
user_weekday = 'szerda'
user_num = 3
user_hianyzasok = 0
for hianyzas in hianyzasok:
    current_date = hianyzas['datum'].split('-')
    if hetnapja(int(current_date[0]), int(current_date[1])) == user_weekday:
        if hianyzas['hianyzasok'][user_num - 1] == "X" or hianyzas['hianyzasok'][user_num - 1] == "I":
            user_hianyzasok += 1

print(f'Ekkor összesen {user_hianyzasok} óra hiányzás történt.')
tanulok = {}
for hianyzas in hianyzasok:
    for letter in hianyzas['hianyzasok']:
        if letter == 'X' or letter=='I':
            if hianyzas['nev'] not in tanulok.keys():
                tanulok[hianyzas['nev']] = 1
            else: tanulok[hianyzas['nev']] += 1

top_missings = []
top_missing_count = sorted(tanulok.items(), key=lambda x: x[1], reverse=True)[0][1]
for item in sorted(tanulok.items(), key=lambda x: x[1], reverse=True):
    if item[1] == top_missing_count: top_missings.append(item[0])
print(top_missings)
