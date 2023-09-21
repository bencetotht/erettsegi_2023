depths = []
with open('melyseg.txt', 'r', encoding='utf8') as f:
    [depths.append(line.strip().split()) for line in f.readlines()]

maxs = depths[:2]
depths = depths[2:]

user_row = int(input('2. feladat\nA mérés sorának azonosítója= '))
user_col = int(input('A mérés oszlopának azonosítója= '))

print(f'A mért mélység az adott helyen {depths[user_row + 1][user_col + 1]} dm')

felszin = 0
melyseg_sum = 0
max_depth = [{'row': 0, 'column': 0, 'depth' : 0}]
for index_r in range(len(depths)):
    for index_c in range(len(depths[index_r])):
        if int(depths[index_r][index_c]) != 0:
            melyseg_sum += int(depths[index_r][index_c])
            felszin += 1
        if max_depth[0]['depth'] < int(depths[index_r][index_c]):
            max_depth[0]['depth'] = int(depths[index_r][index_c])
            max_depth[0]['row'] = int(index_r)
            max_depth[0]['column'] = int(index_c)

print(f'3. feladat\nA tó felszíne: {felszin} m2, átlagos mélysége: {round((melyseg_sum / felszin / 10), 2)} m ')

for index_r in range(len(depths)):
    for index_c in range(len(depths[index_r])):
        if int(depths[index_r][index_c]) == max_depth[0]['depth'] and max_depth[0]['row'] != index_r and max_depth[0]['column'] != index_c:
            max_depth.append({'row': index_r, 'column': index_c, 'depth' : int(depths[index_r][index_c])})

print(f'4. feladat\nA tó legnagyobb mélysége: {max_depth[0]["depth"]} dm\nA legmélyebb helyek sor-oszlop koordinátái:')
[print(f'({depth["row"] + 1}; {depth["column"] + 1})', end='\t') for depth in max_depth]

ossz_kerulet = 0
for index_r, row in enumerate(depths):
    for index_c, col in enumerate(row):
        if int(col) != 0:
            if depths[index_r - 1][index_c] == 0: #fent
                ossz_kerulet += 1
            if int(depths[index_r + 1][index_c]) == 0: #lent
                ossz_kerulet += 1
            if int(row[index_c - 1]) == 0: #balra
                ossz_kerulet += 1
            if int(row[index_c + 1]) == 0: #jobbra
                ossz_kerulet += 1

print(ossz_kerulet)

user_write_col = int(input('\n6. feladat\nA vizsgált szelvény oszlopának azonosítója= '))
with open('diagram.txt', 'w', encoding='utf8') as f:
    for index_r in range(len(depths)):
        print_row = index_r
        if print_row < 10:
            print_row = f'0{index_r}'
        print(print_row, end='', file=f)
        print('*'*int(depths[index_r][user_write_col - 1]), file=f)

