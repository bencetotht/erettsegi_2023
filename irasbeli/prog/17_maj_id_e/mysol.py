records = []
with open('baddaten.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        sor = line.strip().split()
        records.append({
            'vendeg': sor[0],
            'reszleg': sor[1],
            'irany': 'be' if sor[2] == '0' else 'ki',
            'o': int(sor[3]),
            'p': int(sor[4]),
            'mp': int(sor[5]),
            'ido': int(sor[3]) * 3600 + int(sor[4]) * 60 + int(sor[5])
        })

reszleg_szam = {}

for data in records:
    if data['vendeg'] == records[0]['vendeg'] and data['irany'] == 'ki' and data['reszleg'] == '0':
        print(f"Az első vendég {data['o']}:{data['p']}:{data['mp']}-kor lépett ki az öltözőből.")
    if data['vendeg'] == records[-1]['vendeg'] and data['irany'] == 'ki' and data['reszleg'] == '0':
        print(f"Az utolsó vendég {data['o']}:{data['p']}:{data['mp']}-kor lépett ki az öltözőből.")

    if data['vendeg'] not in reszleg_szam.keys():
        reszleg_szam[data['vendeg']] = 1
    else:
        reszleg_szam[data['vendeg']] += 1

mennyiseg = [data for data in reszleg_szam if reszleg_szam[data] == 4]
print(len(mennyiseg))

vendeg_ido = {}
vendeg_ido_szanua = {}
for index, data in enumerate(records):
    if data['vendeg'] not in vendeg_ido: 
        vendeg_ido[data['vendeg']] = [data['ido']] 
    else:
        vendeg_ido[data['vendeg']].append(data['ido'])
    if data['reszleg'] == '2':
        if data['vendeg'] not in vendeg_ido_szanua: 
            vendeg_ido_szanua[data['vendeg']] = [data['ido']] 
        else:
            vendeg_ido_szanua[data['vendeg']].append(data['ido'])

legtobb_ido = 0
legtobb_vendeg = 0
for vendeg in vendeg_ido:
    eltoltott_ido = max(vendeg_ido[vendeg])-min(vendeg_ido[vendeg])
    if eltoltott_ido > legtobb_ido:
        legtobb_ido = eltoltott_ido
        legtobb_vendeg = vendeg

print(legtobb_vendeg, legtobb_ido // 3600, (legtobb_ido % 3600) // 60, ((legtobb_ido % 3600) % 60))

erkezett = [0, 0, 0]
for data in records:
    if data['reszleg'] == '0' and data['irany'] == 'be':
        if (6*3600) < data['ido'] < (8*3600+59*60+59):
            erkezett[0] += 1
        if (9*3600) < data['ido'] < (15*3600+59*60+59):
            erkezett[1] += 1
        if (16*3600) < data['ido'] < (19*3600+59*60+59):
            erkezett[2] += 1

with open('szauna.txt', 'w', encoding='utf8') as f:
    for vendeg in vendeg_ido_szanua:
        eltoltott_ido = 0
        if len(vendeg_ido_szanua[vendeg]) == 2:
            eltoltott_ido = max(vendeg_ido_szanua[vendeg])-min(vendeg_ido_szanua[vendeg])
        else:
            for i in range(0, len(vendeg_ido_szanua[vendeg]) - 1, 2):
                eltoltott_ido += vendeg_ido_szanua[vendeg][i+1] - vendeg_ido_szanua[vendeg][i]

        print(vendeg, eltoltott_ido // 3600, (eltoltott_ido % 3600) // 60, ((eltoltott_ido % 3600) % 60), file=f)
                
reszlegek = {'1': 0, '2': 0, '3': 0, '4': 0}

first_set = set()
second_set = set()
third_set = set()
fourth_set = set()
for data in records:
    if data['reszleg'] == '1' and data['irany'] == 'be' and data['vendeg'] not in first_set:
        first_set.add(data['vendeg'])
        reszlegek[data['reszleg']] += 1
    if data['reszleg'] == '2' and data['irany'] == 'be' and data['vendeg'] not in second_set:
        second_set.add(data['vendeg'])
        reszlegek[data['reszleg']] += 1
    if data['reszleg'] == '3' and data['irany'] == 'be' and data['vendeg'] not in third_set:
        third_set.add(data['vendeg'])
        reszlegek[data['reszleg']] += 1
    if data['reszleg'] == '4' and data['irany'] == 'be' and data['vendeg'] not in fourth_set:
        fourth_set.add(data['vendeg'])
        reszlegek[data['reszleg']] += 1

print(reszlegek)