szakaszok = ['F5.3', 'NF1', 'NF0.6', 'NF0', 'F2.1', 'NF2']

tav = 0
for szakasz in szakaszok:
    if szakasz[0] == 'F':
        tav += float(szakasz[1:])
    else:
        tav += float(szakasz[2:])

megallt = 0
szunet = 0
for szakasz in szakaszok:
    if szakasz == 'NF0':
        megallt += 1

for index in range(len(szakaszok) - 1):
    if szakaszok[index][0] == 'F' and szakaszok[index+1][0:2] == 'NF':
        szunet += 1
    if szakaszok[index][0:2] == 'NF' and float(szakaszok[index][2:]) != 0 and szakaszok[index+1] == 'NF0':
        print('gyaloglas utan megallt')