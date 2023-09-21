szam = ''
while len(str(szam)) < 5:
    szam = int(input('szam: '))

if szam % 10 == 0 and szam % 5 == 0:
    print('erre gondoltal')

print(str(szam)[::-1])

paros = []
[paros.append(szamjegy) for szamjegy in str(szam) if int(szamjegy) % 2 == 0]
print(sorted(paros))

ismetlodo = []
for szamjegy in str(szam):
    if str(szam).count(szamjegy) > 1 and szamjegy not in ismetlodo:
        ismetlodo.append(szamjegy)

print(ismetlodo)

for index, szamjegy in enumerate(str(szam), start=1):
    print('x', end='')
    if (len(str(szam)) - index) % 3 == 0 and len(str(szam)) != index:
        print('.', end='')