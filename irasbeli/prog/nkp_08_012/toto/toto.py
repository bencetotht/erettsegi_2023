#!/usr/bin/env python3

import random

def x12(gól1, gól2):
    if gól1 > gól2:
        return '1'
    elif gól2 > gól1:
        return '2'
    else:
        return 'X'

def csapatot_sorsol(csapatnevek, voltak_már):
    csapatnév = random.choice(csapatnevek)
    while csapatnév in voltak_már:
        csapatnév = random.choice(csapatnevek)
    return csapatnév

def gólkülönbség(mérkőzés):
    return abs(mérkőzés['gól_1']-mérkőzés['gól_2'])

csapatnevek = []
with open('csapatnevek.txt', encoding='utf-8') as forrásfájl:
    for sor in forrásfájl:
        csapatnevek.append(sor.strip())

voltak_már = []
szelvény = []
for _ in range(7):
    mérkőzés = {}
    mérkőzés['csapat_1'] = csapatot_sorsol(csapatnevek, voltak_már)
    voltak_már.append(mérkőzés['csapat_1'])
    mérkőzés['csapat_2'] = csapatot_sorsol(csapatnevek, voltak_már)
    voltak_már.append(mérkőzés['csapat_2'])
    mérkőzés['gól_1'] = random.randint(0, 5)
    mérkőzés['gól_2'] = random.randint(0, 5)
    szelvény.append(mérkőzés)

mérkőzés = {}
nevek = input('Adja meg a két csapat nevét! ')
mérkőzés['csapat_1'], mérkőzés['csapat_2'] = nevek.split('-')
eredmény = input('Adja meg az eredményt! ')
mérkőzés['gól_1'], mérkőzés['gól_2'] = map(int, eredmény.split(':'))
szelvény.append(mérkőzés)

print('\nGergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
for mérkőzés in szelvény:
    print(f"{mérkőzés['csapat_1']} - {mérkőzés['csapat_2']} ",
        f"{mérkőzés['gól_1']}:{mérkőzés['gól_2']}",
        f"{x12(mérkőzés['gól_1'], mérkőzés['gól_2'])}")

with open('szelveny.txt', 'w', encoding='utf-8') as célfájl:
    print('\nGergelyiugornyai totó, 53. hét, telitalálatos szelvény:',
        file=célfájl)
    for mérkőzés in szelvény:
        print(f"{mérkőzés['csapat_1']} - {mérkőzés['csapat_2']} ",
            f"{mérkőzés['gól_1']}:{mérkőzés['gól_2']}",
            f"{x12(mérkőzés['gól_1'], mérkőzés['gól_2'])}", file=célfájl)

gólkülönbségek = []
for mérkőzés in szelvény:
    gólkülönbségek.append(gólkülönbség(mérkőzés))
legnagyobb_gólkülönbség = max(gólkülönbségek)
print('\nLegnagyobb gólkülönbségű mérkőzések: ', end='')
for index, gólkülönbség in enumerate(gólkülönbségek):
    if gólkülönbség == legnagyobb_gólkülönbség:
        if index <= 6:
            print(index+1, end=' ')
        else:
            print('+1', end='')
print('')

print('\n0:0-ás mérkőzések: ', end='')
for index, mérkőzés in enumerate(szelvény):
    if mérkőzés['gól_1'] == 0 and mérkőzés['gól_2'] == 0:
        if index <= 6:
            print(index+1, end=' ')
        else:
            print('+1', end='')
print('')

legalább_két_gólos_győztesek = []
for mérkőzés in szelvény:
    if mérkőzés['gól_1'] >= mérkőzés['gól_2'] + 2:
        legalább_két_gólos_győztesek.append(mérkőzés['csapat_1'])
    elif mérkőzés['gól_2'] >= mérkőzés['gól_1'] + 2:
        legalább_két_gólos_győztesek.append(mérkőzés['csapat_2'])
if legalább_két_gólos_győztesek:
    print('\nLegalább két góllal nyertek: ',
        ', '.join(legalább_két_gólos_győztesek))
