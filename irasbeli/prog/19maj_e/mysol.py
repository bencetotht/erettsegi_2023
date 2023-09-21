data = []
with open('autok.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        sor = line.strip().split()
        data.append({
            'nap': sor[0],
            'ido': sor[1],
            'rendszam': sor[2],
            'szemely': sor[3],
            'km': sor[4],
            'irany': sor[5],
        })

utolso_auto = 0
for rec in data:
    if rec['irany'] == '0': utolso_auto = rec['rendszam']

print(f'2. feladat\n30. nap rendszám: {utolso_auto}')

# user_nap = input('\n3. feladat\nNap: ')
user_nap = '4'
print(f'Forgalom a(z) {user_nap}. napon:')
autok_out = []
autok_tav = {}
for rec in data:
    if rec['nap'] == user_nap:
        print(f"{rec['ido']} {rec['rendszam']} {rec['szemely']} {rec['irany']}")
    if rec['irany'] == '0': autok_out.append(rec['rendszam'])
    elif rec['irany'] == '1': autok_out.remove(rec['rendszam'])

    if autok_tav.get(rec['rendszam']):
        autok_tav[rec['rendszam']]['vegso'] = rec['km']
    else:
        autok_tav[rec['rendszam']] = {'kezdo': rec['km'], 'vegso': rec['km']}

print(f'\n4. feladat\nA hónap végén {len(autok_out)} autót nem hoztak vissza. ')

for auto in autok_tav:
    print(auto, int(autok_tav[auto]['vegso'])-int(autok_tav[auto]['kezdo']), 'km')

max_szemely = ''
max_km = 0
for index, rec in enumerate(data):
    if rec['irany'] == '1':
        prev_index = index - 1
        while rec['rendszam'] != data[prev_index]['rendszam']:
            prev_index -= 1
        current_distance = int(rec['km']) - int(data[prev_index]['km'])
        if current_distance > max_km:
            max_km = current_distance
            max_szemely = rec['szemely']
print(f'\n6. feladat\nLeghosszabb út: {max_km} km, személy: {max_szemely} ')

# user_rendszam = input('\n7. feladat\nRendszám: ')
user_rendszam = 'CEG304' 

with open(f'{user_rendszam}_menetlevel.txt', 'w', encoding='utf8') as f:
    for rec in data:
        if rec['rendszam'] == user_rendszam:
            if rec['irany'] == '0': print(f"{rec['szemely']}\t{rec['nap']}. {rec['ido']}\t{rec['km']} km", end='\t', file=f)
            elif rec['irany'] == '1': print(f"{rec['nap']}. {rec['ido']}\t{rec['km']} km", file=f)