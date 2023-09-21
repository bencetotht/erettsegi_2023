# Feladatlap
# https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022tavasz_emelt/e_infma_22maj_fl.pdf
def orara_valt(o, p, msp, ezred_msp):
    return o + (p / 60) + (msp + (ezred_msp / 1000)) / 3600


jarmuvek = []
with open('meresek.txt', 'r') as fajl:
    for sor in fajl:
        adatok = sor.strip().split()
        jarmu = {'rendszam': adatok[0],
                 'be': orara_valt(int(adatok[1]), int(adatok[2]), int(adatok[3]), int(adatok[4])),
                 'ki': orara_valt(int(adatok[5]), int(adatok[6]), int(adatok[7]), int(adatok[8]))}
        jarmuvek.append(jarmu)

print('2. feladat')
print(f'A mérés során {len(jarmuvek)} jármű adatait rögzítették.')

print('3. feladat')
athalad = 0
for jarmu in jarmuvek:
    if jarmu['ki'] < 9:
        athalad += 1
print(f'9 óra előtt {athalad} jármű haladt el a végponti mérőnél.')

print('4. feladat')
ora_perc = ['8', '20']  # input('Adjon meg egy óra és perc értéket! ').strip().split()
meres_kezdete = float(ora_perc[0]) + float(ora_perc[1]) / 60
meres_vege = float(ora_perc[0]) + float(ora_perc[1]) / 60 + 59.999 / 3600
athalad = 0
uton = 0
for jarmu in jarmuvek:
    if meres_kezdete <= jarmu['be'] <= meres_vege:
        athalad += 1
    if meres_vege > jarmu['be'] and meres_kezdete < jarmu['ki']:
        uton += 1
print(f'\ta. A kezdeti méréspontnál elhaladt járművek száma: {athalad}')
print(f'\tb. A forgalomsűrűség: {uton / 10}')

print('5. feladat')
print('A legnagyobb sebességgel haladó jármű')
max_v = 0
max_v_jarmu = {}
for jarmu in jarmuvek:
    v = 10 / (jarmu['ki'] - jarmu['be'])
    if v > max_v:
        max_v = v
        max_v_jarmu = jarmu
print(f'\t rendszáma: {max_v_jarmu["rendszam"]}')
print(f'\t átlagsebessége: {round(max_v)} km/h')
leelozott = 0
for jarmu in jarmuvek:
    if jarmu['be'] < max_v_jarmu['be'] and jarmu['ki'] > max_v_jarmu ['ki']:
        leelozott += 1
print(f'\t által lehagyott járművek száma: {leelozott}')


print('6. feladat')
gyorshajto = 0
for jarmu in jarmuvek:
    v = 10 / (jarmu['ki'] - jarmu['be'])
    if v > 90:
        gyorshajto += 1
print(f'A járművek {gyorshajto / len(jarmuvek) * 100:.2f}%-a volt gyorshajtó.')


def birsag(sebesseg):
    if sebesseg <= 121:
        return 30000
    elif sebesseg <= 136:
        return 45000
    elif sebesseg <= 151:
        return 60000
    else:
        return 200000


print('7. feladat')
with open('buntetes.txt', 'w', encoding='utf-8') as buntetes:
    for jarmu in jarmuvek:
        v = 10 / (jarmu['ki'] - jarmu['be'])
        if v > 104:
            print(f'{jarmu["rendszam"]}\t{round(v)} km/h\t{birsag(v)} Ft ', file=buntetes)

