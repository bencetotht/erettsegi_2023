import math

jelek = []
with open('jel.txt', 'r') as bemenet:
    for sor in bemenet:
        jel = sor.strip().split()
        jelek.append(list(map(int, jel)))


print('2. feladat')
sorszam = int(input('Adja meg a jel sorszámát! '))
print(f'x={jelek[sorszam - 1][3]} y={jelek[sorszam - 1][4]}')

print('3. feladat')


def eltelt(jel1, jel2):
    return abs((jel2[0] - jel1[0]) * 3600 + (jel2[1] - jel1[1]) * 60 + (jel2[2]-jel1[2]))


print('4. feladat')
kulonbseg = eltelt(jelek[0], jelek[-1])
ora = kulonbseg // 3600
perc = (kulonbseg % 3600) // 60
mperc = kulonbseg % 60
print(f'Időtartam: {ora}:{perc}:{mperc}')


print('5. feladat')
minx = 10000
maxx = -10000
miny = 10000
maxy = -10000
for jel in jelek:
    minx = min(minx, jel[3])
    maxx = max(maxx, jel[3])
    miny = min(miny, jel[4])
    maxy = max(maxy, jel[4])
print(f'Bal alsó: {minx} {miny}, jobb felső: {maxx} {maxy}')


print('6. feladat')
jelek_szama = len(jelek)


def tav(jel1, jel2):
    return math.sqrt((jel2[3]-jel1[3])**2 + (jel2[4]-jel1[4])**2)


osszesen = 0
for index in range(jelek_szama - 1):
    osszesen += tav(jelek[index], jelek[index + 1])
print(f'Elmozdulás: {osszesen:0.3f} egység')


print('7. feladat')
with open('kimaradt.txt', 'w', encoding='utf8') as kimenet:
    for index in range(jelek_szama - 1):
        kimaradt_tavolsag_szerint = 0
        kimaradt_ido_szerint = 0

        idokulonbseg = eltelt(jelek[index], jelek[index + 1])
        if idokulonbseg > 300:
            kimaradt_ido_szerint = (idokulonbseg - 1) // 300

        tavolsag = max(abs(jelek[index + 1][3] - jelek[index][3]), abs(jelek[index + 1][4] - jelek[index][4]))
        if tavolsag > 10:
            kimaradt_tavolsag_szerint = (tavolsag - 1) // 10

        if kimaradt_tavolsag_szerint > kimaradt_ido_szerint:
            print(jelek[index+1][0], jelek[index+1][1], jelek[index+1][2], 'koordináta-eltérés', kimaradt_tavolsag_szerint, file=kimenet)
        if kimaradt_tavolsag_szerint <= kimaradt_ido_szerint != 0:
            print(jelek[index+1][0], jelek[index+1][1], jelek[index+1][2], 'időeltérés', kimaradt_ido_szerint, file=kimenet)
