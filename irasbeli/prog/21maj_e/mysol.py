depths = []
with open('melyseg.txt', 'r', encoding='utf8') as f:
    [depths.append(line.strip()) for line in f.readlines()]

print(f'1. feladat\nA fájl adatainak száma: {len(depths)}')

user_input = int(input('\n2. feladat\nAdjon meg egy távolságértéket! '))
print(f'Ezen a helyen a felszín {depths[user_input]} méter mélyen van. ')

sertetlen = 0
for depth in depths:
    if int(depth) == 0:
        sertetlen += 1

print(f'\n3. feladat\nAz érintetlen terület aránya {round((sertetlen / len(depths) * 100), 2)}%.')

depth_count = 0
with open('godrok.txt', 'w', encoding='utf8') as f:
    current_depth = []
    for depth in depths:
        if int(depth) != 0:
            current_depth.append(depth)
        if int(depth) == 0 and len(current_depth) != 0:
            print(' '.join(current_depth), file=f)
            depth_count += 1
            current_depth = []

print(f'\n5. feladat\nA gödrök száma: {depth_count}')

print('\n6. feladat')
if int(depths[user_input]) == 0:
    print('Az adott helyen nincs gödör.')
else:
    # current_start = 0
    # current_end = 0
    # user_cycle = False
    # current_max_depth = 0
    # for index in range(len(depths)):
    #     if current_start == 0 and int(depths[index]) != 0:
    #         current_start = int(depths[index])
    #         current_end = 0
    #     elif current_start != 0 and int(depths[index]) == 0:
    #         current_end = int(depths[index - 1])
    #         current_start = 0
    #     if int(depths[index]) != 0:

    #     if index == user_input:
    #         user_cycle = True
    #         print(f'a)\nA gödör kezdete: {current_start} méter, ', end='')
    #     if user_cycle == True and current_end != 0:
    #         user_cycle = False
    #         print(f'a gödör vége: {current_end} méter.')
    current_depth = []
    for index in range(len(depths)):
        if int(depths[index]) != 0:
            current_depth.append(depths[index])
        if int(depths[index]) == 0 and len(current_depth) != 0:
            print(' '.join(current_depth), file=f)
            current_depth = []

    # TODO finish 6.