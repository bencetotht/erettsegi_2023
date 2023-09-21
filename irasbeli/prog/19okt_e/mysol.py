utasdata = []
with open('utasadat.txt', 'r', encoding='utf8') as f:
    [utasdata.append(line.strip().split()) for line in f.readlines()]

utasok = set()
elutasitas = 0
max_felszallo = 0
felszallok = [0 for _ in range(0, 30)]
jegyek = {'FEB': 0, 'TAB': 0, 'NYB': 0, 'NYP': 0, 'RVS': 0, 'GYK': 0, 'JGY': 0}
for data in utasdata:
    utasok.add(data[2])
    if (data[3] == 'JGY' and int(data[4]) == 0) or (data[3] != 'JGY' and data[1].split('-')[0] > data[4]):
        elutasitas += 1
    else:
        jegyek[data[3]] += 1
    felszallok[int(data[0])] += 1

print(f"2. feladat\nA buszra {len(utasok)} utas akart felszállni.\n3. feladat\nA buszra {elutasitas} utas nem szállhatott fel\n4. feladat\nA legtöbb utas ({max(felszallok)} fő) a {felszallok.index(max(felszallok))}. megállóban próbált felszállni.\n5. feladat\nIngyenesen utazók száma: {jegyek['NYP'] + jegyek['RVS'] + jegyek['GYK']} fő\nA kedvezményesen utazók száma: {jegyek['TAB'] + jegyek['NYB']} fő")

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1

with open('figyelmeztetes.txt', 'w', encoding='utf8') as f:
    for data in utasdata:
        current_date = data[1].split('-')[0]
        expire_date = data[4]
        if len(expire_date) == 8:
            if napokszama(int(current_date[0:4]), int(current_date[4:6]), int(current_date[6:]), int(expire_date[0:4]), int(expire_date[4:6]), int(expire_date[6:])) <= 3:
                print(f"{data[2]} {expire_date[0:4]}-{expire_date[4:6]}-{expire_date[6:]}", file=f)