import random
dobasok = [random.randint(1,6) for _ in range(int(input('1. feladat\nAdd meg a dobások számát! ')))]

print(f'\n2. feladat\nA dobások: {dobasok}')
print(f'\n3. feladat\nA játékos átlagosan {sum(dobasok) / len(dobasok)} mezőt, összesen {sum(dobasok)} mezőt haladt előre.')

hatosok = 0
paros = 0
for dobas in dobasok:
    if dobas == 6: hatosok += 1
    if dobas % 2 == 0: paros += 1
if hatosok != 0: print(f'\n4. feladat\nA játékos {hatosok} alkalommal dobott hatost.')
else: print('\n4. feladat\nA játékos sajnos egy alkalommal sem dobott hatost.')
if paros != 0: print(f'\n5. feladat\nA játékos {paros} alkalommal dobott páros számot.')
else: print('\n5. feladat\nA játékos sajnos egy alkalommal sem dobott páros számot.')

kisebb_dobasok = 0
for i in range(len(dobasok) - 1):
    if dobasok[i] > dobasok[i+1]: kisebb_dobasok += 1

print(f'\n6. feladat\nA játékos {kisebb_dobasok} alkalommal dobott kevesebbet, mint előző körben.')