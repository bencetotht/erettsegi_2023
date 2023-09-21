# userFile = input('1. feladat\nAdja meg a bemeneti fájl nevét! ')
userFile = 'konnyu.txt'
table = []
moves = []
with open(userFile, 'r', encoding='utf8') as f:
    for line in f.readlines():
        line_p = line.strip().split()
        if len(line_p) == 9: table.append(line_p)
        elif len(line_p) == 3: moves.append(line_p)

user_sor = int(input('Adja meg egy sor számát! ')) -1
user_oszlop = int(input('Adja meg egy oszlop számát! ')) -1
user_output = table[user_sor][user_oszlop]
if user_output == 0: print('Az adott helyet még nem töltötték ki.')
else: print(user_output)

print(f'{3 * (user_oszlop // 3) + (user_sor // 3) + 1}')

empty = 0
for sor in table:
    for value in sor:
        if int(value) == 0:
            empty += 1

print(f'\n\n4. feladat\nAz üres helyek aránya: {round((empty / 81 * 100), 1)}%')

print('\n\n5. feladat')
for move in moves:
    current_sor = move[1]
    current_oszlop = move[2]
    current_number = move[0]

    print(f'\nA kiválasztott sor: {move[1]} oszlop: {move[2]} a szám: {move[0]}')

    for value in table[int(move[1]) - 1]:
        if int(value) == int(move[0]): print('Az adott sorban már szerepel a szám')
    for sor in table:
        if int(sor[int(move[2]) - 1]) == int(move[0]): print('Az adott oszlopban már szerepel a szám')
    if int(table[int(move[1]) - 1][int(move[2]) - 1]) != 0: print('A helyet már kitöltötték')
