meresek = []
with open('meresek.txt', encoding='utf8') as f:
    [meresek.append(line.strip().split()) for line in f.readlines()]

print(f'2. feladat\nA mérés során {len(meresek)} jármű adatait rögzítették.')

before_nine = []
for meres in meresek:
    if int(meres[5]) < 9:
        before_nine.append(meres)

print(f'\n3. feladat\n9 óra előtt {len(before_nine)} jármű haladt el a végponti mérőnél.')

def convertTime(h, m, s, ms):
    return int(h)+(float(m)/60)+((float(s)+(float(ms)/1000))/3600)

userTime = input('\n4. feladat\nAdjon meg egy óra és perc értéket! ').split()
user_count = 0
athalado = 0
for meres in meresek:
    if int(meres[1]) == int(userTime[0]) and int(meres[2]) == int(userTime[1]):
        user_count += 1
    if convertTime(meres[1], meres[2], meres[3], meres[4]) <= convertTime(userTime[0], userTime[1], '0', '0') and convertTime(meres[5], meres[6], meres[7], meres[8]) >= convertTime(userTime[0], userTime[1], '59', '599'):
        athalado += 1
print(f'\ta. A kezdeti méréspontnál elhaladt járművek száma: {user_count}')
print(f'\tb. A forgalomsűrűség: {athalado / 10}')


def calc_speed(time1, time2):
    return 10 / (time2 - time1)

fastest_record = []
fastest_speed = 0
for meres in meresek:
    meres_speed = calc_speed(convertTime(meres[1], meres[2], meres[3], meres[4]), convertTime(meres[5], meres[6], meres[7], meres[8]))
    if meres_speed > fastest_speed:
        fastest_speed = meres_speed
        fastest_record = meres

elozott = 0
for meres in meresek:
    if convertTime(meres[1], meres[2], meres[3], meres[4]) < convertTime(fastest_record[1], fastest_record[2], fastest_record[3], fastest_record[4]) and convertTime(meres[5], meres[6], meres[7], meres[8]) > convertTime(fastest_record[5], fastest_record[6], fastest_record[7], fastest_record[8]):
        elozott += 1

print(f'\n5. feladat\nA legnagyobb sebességgel haladó jármű\n\trendszáma: {fastest_record[0]}\n\tátlagsebessége: {int(fastest_speed)} km/h\n\táltal lehagyott járművek száma: {elozott}')

meghaladta = 0
for meres in meresek:
    if calc_speed(convertTime(meres[1], meres[2], meres[3], meres[4]), convertTime(meres[5], meres[6], meres[7], meres[8])) > 90:
        meghaladta += 1

print(f'\n6. feladat\nA járművek {round((meghaladta / len(meresek)) * 100, 2)}%-a volt gyorshajtó.')

def calc_penalty(meres):
    speed =  calc_speed(convertTime(meres[1], meres[2], meres[3], meres[4]), convertTime(meres[5], meres[6], meres[7], meres[8]))
    
    if speed < 104:
        return '0'
    elif 104 <= speed < 121:
        return '30 000 Ft'
    elif 121 <= speed < 136:
        return '45 000 Ft'
    elif 136 <= speed < 151:
        return '60 000 Ft'
    elif 151 <= speed:
        return '200 000 Ft'
    


with open('buntetes.txt', 'w', encoding='utf8') as f:
    for meres in meresek:
        if calc_penalty(meres) != '0':
            print(f'{meres[0]}\t{round(calc_speed(convertTime(meres[1], meres[2], meres[3], meres[4]), convertTime(meres[5], meres[6], meres[7], meres[8])))} km/h\t{calc_penalty(meres)}', file=f)
