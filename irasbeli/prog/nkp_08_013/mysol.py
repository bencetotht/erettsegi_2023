dobozok = []
max_doboz = 0
max_jatek = 0
with open('dobozok.txt', 'r', encoding='utf8') as f:
    for index,line in enumerate(f.readlines()):
        sor = line.strip().split()
        if index == 0:
            max_doboz = int(sor[0])
            max_jatek = int(sor[1])
        else:
            dobozok.append({'szam': int(sor[0]), 'jatek': sor[1:]})

osszeg = 0
for doboz in dobozok:
    osszeg += doboz['szam']
atlag = osszeg / max_doboz
print(atlag)

asc = sorted(dobozok, key=lambda d: d['szam'])
legtobb_jatek = asc[-1]['szam']
legtobb_jatek_dobozok = []
for doboz in dobozok:
    if int(doboz['szam']) == legtobb_jatek: legtobb_jatek_dobozok.append(dobozok.index(doboz) + 1)

print(legtobb_jatek_dobozok)
jatekok = {}
for doboz in dobozok:
    for jatek in doboz['jatek']:
        if jatek not in jatekok:
            jatekok[jatek] = 1
        else: jatekok[jatek] += 1
desc_jatekok = sorted(jatekok.items(), key=lambda d: d[1], reverse=True)
top_jatekok = []
for jatek in desc_jatekok:
    if jatek[1] == desc_jatekok[1][1]: top_jatekok.append(jatek[0])

print(top_jatekok)
for doboz in dobozok:
    if int(doboz['szam']) > atlag:
        print(f"{dobozok.index(doboz)+1}. dobozból {round(abs(int(doboz['szam']) - atlag))} db játékot")

with open('berakhato.txt', 'w', encoding='utf8') as f:
    osszes_jatek = [str(i) for i in range(1, max_jatek + 1)]
    for doboz in dobozok:
        if int(doboz['szam']) < atlag: 
            print(f"\n{dobozok.index(doboz) + 1}. doboz: ", end="", file=f)
            for jatek in osszes_jatek:
                if jatek not in doboz['jatek']:
                    print(jatek, end=" ", file=f)