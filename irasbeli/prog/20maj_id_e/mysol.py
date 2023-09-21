data = []
with open('vonat.txt', 'r', encoding='utf8') as f:
    [data.append(line.strip().split()) for line in f.readlines()]

vonatok = set()
allomasok = set()
for row in data:
    if row[0] not in vonatok: vonatok.add(row[0])
    if row[1] not in allomasok: allomasok.add(row[1])

print(f'2. feladat\nAz állomások száma: {len(allomasok)}\nA vonatok száma: {len(vonatok)} ')


longest_station = {
    'vonat': '',
    'allomas': '',

}
# for index in range(len(data) - 1):
    # print(data[index][4], data[index + 1][4])

# user_vonat = input('\n\n4. feladat\nAdja meg egy vonat azonosítóját! ')
# user_ido = input('Adjon meg egy időpontot (óra perc)! ').split(' ')

user_vonat = '2'
user_ido = [6, 50]

start_time = 10000
end_time = 0
route = 2*60+22
for row in data:
    if row[0] == user_vonat:
        if (int(row[2]) * 60 + int(row[3])) < start_time:
            start_time = int(row[2]) * 60 + int(row[3])
        end_time = int(row[2]) * 60 + int(row[3])

if route == (end_time - start_time): print('pontos')
elif route < (end_time - start_time): print(f'lassabb, {(end_time - start_time) - route}')
elif route > (end_time - start_time): print(f'gyorsabb, {route - (end_time - start_time)}')

with open(f'halad{user_vonat}.txt', 'w', encoding='utf8') as f:
    allomas_index = 1
    for row in data:
        if row[0] == user_vonat and row[4] == 'E': 
            print(f'{allomas_index}. állomás: {row[2]}:{row[3]}', file=f)
            allomas_index += 1


for row_train in data:

    for row in data:
        if row_train[0] == row[0] and 
    user_time = user_ido[0]*60 + user_ido[1]
    current_time = int(row[2]) * 60 + int(row[3])