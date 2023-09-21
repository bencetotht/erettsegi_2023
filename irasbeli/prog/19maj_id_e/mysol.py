data = []
insert = []
with open('beosztas.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        insert.append(line.strip())
        if len(insert) == 4: 
            data.append({'tanar': insert[0], 'tantargy': insert[1], 'osztaly': insert[2], 'ora': int(insert[3])})
            insert = []

print(f'2. feladat\nA fájlban {len(data)} bejegyzés van. ')
ora_sum = 0 
for record in data:
    ora_sum += record['ora']

print(f'\n3. feladat\nAz iskolában a heti összóraszám: {ora_sum} ')

# user_tanar = input('\n4. feladat\nEgy tanár neve= Albatrosz Aladin ')
user_tanar = 'Albatrosz Aladin'

tanar_sum = 0
for record in data:
    if record['tanar'] == user_tanar: tanar_sum += record['ora']
print(f'A tanár heti óraszáma: {tanar_sum}')

with open('of.txt', 'w', encoding='utf8') as f:
    tanar_already = set()
    for record in data:
        if record['tanar'] not in tanar_already and record['tantargy'] == 'osztalyfonoki':
            tanar_already.add(record['tanar'])
            print(f"{record['osztaly']} - {record['tanar']}", file=f)

# user_osztaly = input('\n6. feladat\nOsztály= ')
# user_tantargy = input('Tantárgy= ')
user_osztaly = '10.b'
user_tantargy = 'kemia'
user_tantargy_num = 0
tanarok = set()
for record in data:
    if record['tanar'] not in tanarok: tanarok.add(record['tanar'])
    if record['tantargy'] == user_tantargy and record['osztaly'] == user_osztaly: user_tantargy_num += 1
if user_tantargy_num == 2: print('Csoportbontásban tanulják.')
elif user_tantargy_num == 1: print('Nem csoportbontásban tanulják.')

print(f'\n7. feladat\nAz iskolában {len(tanarok)} tanár tanít. ')