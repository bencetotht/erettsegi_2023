data = []
with open('lista.txt', 'r', encoding='utf8') as f: 
    tempdata=[]
    for row in f.readlines():
        tempdata.append(row.strip())
        if len(tempdata) == 5:
            data.append({
                'date': tempdata[0],
                'name': tempdata[1],
                'ep': tempdata[2],
                'length': tempdata[3],
                'seen': tempdata[4]
            })
            tempdata = []

date_sum = seen_sum = seen_time = 0
for movie in data:
    if movie['date'] != 'NI': date_sum += 1
    if movie['seen'] == '1': 
        seen_sum += 1
        seen_time += int(movie['length'])


print(f'2. feladat\nA listában {date_sum} db vetítési dátummal rendelkező epizód van. \n\n3. feladat\nA listában lévő epizódok {round(seen_sum / len(data) * 100, 2)}%-át látta. \n\n4. feladat\nSorozatnézéssel {seen_time // (60 * 24)} napot {(seen_time % (60 * 24)) // 60} órát és {seen_time % 60} percet töltött. ')
date = input('\n\n5. feladat\nAdjon meg egy dátumot! Dátum= ')
for movie in data:
    if movie['date'] <= date and movie['seen'] == '0':
        print(f"{movie['ep']} \t {movie['name']}")

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3: ev -= 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]

user_nap = input('\n\n7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ')
series_on_day = set()
for movie in data:
    if movie['date'] != 'NI':
        if hetnapja(int(movie['date'][0:4]), int(movie['date'][5:7]), int(movie['date'][8:10])) == user_nap:
            series_on_day.add(movie['name'])
if(len(series_on_day)) != 0: 
    for series in series_on_day: print(series)
else: 
    print('Az adott napon nem kerül adásba sorozat.')

with open('summa.txt', 'w', encoding='utf8') as f:
    already_counted = []
    for movie in data: 
        current_minutes = 0
        current_eps = 0
        if movie['name'] not in already_counted:
            for movie2 in data:
                if movie2['name'] == movie['name']:
                    current_eps += 1
                    current_minutes += int(movie['length'])
            already_counted.append(movie['name'])
            print(f"{movie['name']} {current_minutes} {current_eps}", file=f)
