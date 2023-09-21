import math

signals = []
with open('jel.txt', encoding='utf8') as f:
    [signals.append(list(map(int, line.strip().split()))) for line in f.readlines()]

num = int(input('2.feladat\nWhich one would you like to see?'))
if num <= len(signals):
    print(f'x: {signals[num - 1][3]} y: {signals[num - 1][4]}')
else:
    print('too high value')

def timeBetween(timeFrom, timeTo):
    return (((timeTo[0] - timeFrom[0]) * 3600) + ((timeTo[1] - timeFrom[1]) * 60) + (timeTo[2] - timeFrom[2]))

firstAndLast = timeBetween(signals[0], signals[-1])
print(f'\n4. feladat\n{firstAndLast // 3600}:{(firstAndLast%3600) // 60}:{(firstAndLast%3600)%60}')

minX = minY = 10000
maxX = maxY = -10000
for signal in signals:
    minX = min(minX, signal[3])
    minY = min(minY, signal[4])
    maxX = max(maxX, signal[3])
    maxY = max(maxY, signal[4])
print(f'\n5.feladat\nBal alsó: {minX} {minY}, jobb felső: {maxX} {maxY}')

def dist(signal1, signal2):
    return math.sqrt(pow((signal2[3] - signal1[3]), 2) + pow((signal2[4] - signal1[4]), 2))

sum=0
for index in range(len(signals) - 1):
    sum += dist(signals[index], signals[index + 1])

print(f'\n6.feladat\nElmozdulás: {round(sum, 2)} egység')

with open('kimaradt.txt', 'w', encoding='utf8') as f:


    for index in range(len(signals) - 1):
        missed_time = missed_dist = 0
        time = timeBetween(signals[index], signals[index + 1])
        distance= dist(signals[index], signals[index + 1]) 
        if time > 300:
            missed_time = time // 300
        
        if distance > 10:
            missed_dist = distance // 10
        
        if missed_dist > missed_time:
            print(f'{signals[index + 1][0]} {signals[index + 1][1]} {signals[index + 1][2]} koordináta-eltérés {round(missed_dist)}', file=f)
        if missed_dist <= missed_time != 0:
            print(f'{signals[index + 1][0]} {signals[index + 1][1]} {signals[index + 1][2]} időeltérés {missed_time}', file=f)