print('1. feladat')
eladasok, ans = [], 0
while ans != '':
    ans = input('Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23): ')
    if ans != '': eladasok.append(ans)
sum = max_d = 0
for eladas in eladasok:
    sum += int(eladas[1:])
    if eladas[0].lower() == 'd' and max_d < int(eladas[1:]): max_d = int(eladas[1:])
print(f'\n2. feladat\nA benzinkúton {len(eladasok)} alkalommal vásároltak.\n\n3. feladat\n{sum}l benzint adtak el összesen.\n\n4. feladat\nEgy alkalommal átlagosan {round(sum / len(eladasok), 2)}l üzemanyagot vásároltak.\n\n5. feladat\nAz egy alkalommal eladott legnagyobb diesel mennyiség {max_d}l volt.')