fogadasok = []
with open('fogado.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        sor = line.strip().split()
        fogadasok.append({'tanar': f'{sor[0]} {sor[1]}', 'idopont': sor[2], 'datum': sor[3]})
print(f'2. feladat\nFoglalások száma: {len(fogadasok)} ')

# user_tanar = input('\n3. feladat\nAdjon meg egy nevet: ')
user_tanar = 'Nagy Ferenc'
user_tanar_count = 0
for data in fogadasok:
    if data['tanar'] == user_tanar: user_tanar_count += 1
if user_tanar_count == 0: print('A megadott néven nincs időpontfoglalás')
else: print(f'Nagy Ferenc néven {user_tanar_count} időpontfoglalás van.')

# user_idopont = input('\n4. feladat\nAdjon meg egy érvényes időpontot (pl. 17:10): ')
user_idopont = '17:40'
tanarok = []
tanar_foglalt = []
osszes_idopont = []
for i in range(6, 8):
    for j in range(0, 6):
        osszes_idopont.append(f'1{i}:{j}0')
legkorabbi = {'tanar': '', 'idopont': '', 'datum': '2017.10.28-18:48', 'datum_i': ''}
for data in fogadasok:
    if data['idopont'] == user_idopont: 
        tanarok.append(data['tanar'])

    if legkorabbi['datum'] > data['datum']:
        print(legkorabbi['datum'], data['datum'])
        legkorabbi['datum'] = data['datum']

    if data['tanar'] == 'Barna Eszter':
        osszes_idopont.remove(data['idopont'])

print(osszes_idopont)
# print('\n'.join(sorted(tanarok)))

with open(f"{user_idopont.replace(':', '')}.txt", 'w', encoding='utf8') as f:
    print('\n'.join(sorted(tanarok)), file=f)
