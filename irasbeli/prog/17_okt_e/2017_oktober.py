"""
2017. október - Hiányzások
https://sulipy.hu/erettsegi
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2017osz_emelt/e_inf_17okt_fl.pdf
"""
# Adatstrukúra
# naplo = {
#     '04 02': {'Alma Hedvig': 'OOOOOIO',
#               'Galagonya Alfonz': 'XXXXXXX'},
#     ...
# }

naplo = {}
diak = []
with open('naplo.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        if sor[0] == '#':
            datum_sor = sor.strip().split()
            datum = datum_sor[1] + ' ' + datum_sor[2]
            naplo[datum] = {}
        else:
            bejegyzes = sor.strip().split()
            nev = bejegyzes[0] + ' ' + bejegyzes[1]
            naplo[datum][nev] = bejegyzes[2]
print(naplo)


print('2. feladat')
szamlalo = 0
for datum in naplo:
    szamlalo += len(naplo[datum])
print(f'A naplóban {szamlalo} bejegyzés van. ')


print('3. feladat')
igazolt = 0
igazolatlan = 0
for datum in naplo:
    for diak in naplo[datum]:
        igazolt += naplo[datum][diak].count('X')
        igazolatlan += naplo[datum][diak].count('I')
print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')


print('4. feladat')
def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]


# print('5. feladat')
# honap_ssz = int(input('A hónap sorszáma= '))
# nap_ssz = int(input('A nap sorszáma= '))
# print(f'Azon a napon {hetnapja(honap_ssz, nap_ssz)} volt. ')


print('6. feladat')
nap_neve = 'szerda' # input('A nap neve=')
ora = 3 # int(input('Az óra sorszáma='))
hianyzas = 0
for datum in naplo:
    if hetnapja(int(datum[:2]), int(datum[3:])) == nap_neve:
        for diak in naplo[datum]:
            if 'X' in naplo[datum][diak][ora-1] or 'I' in naplo[datum][diak][ora-1]:
                hianyzas += 1
                print(datum, diak, naplo[datum][diak][ora-1])
print(f'Ekkor összesen {hianyzas} óra hiányzás történt.')


print('7. feladat')
hianyzok = {}
for datum in naplo:
    for diak in naplo[datum]:
        hianyzas = naplo[datum][diak].count('X') + naplo[datum][diak].count('I')
        if diak in hianyzok:
            hianyzok[diak] += hianyzas
        else:
            hianyzok[diak] = hianyzas

max_hianyzas = 0
for diak in hianyzok:
    if hianyzok[diak] > max_hianyzas:
        max_hianyzas = hianyzok[diak]
for diak, oraszam in hianyzok.items():
    if oraszam == max_hianyzas:
        print(diak, end=' ')
