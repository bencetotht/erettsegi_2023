plots = []

with open('utca.txt', 'r', encoding='utf8') as f:
    [plots.append(line.strip().split()) for line in f.readlines()]

costs = plots.pop(0)
print(f'2. feladat. A mintában {len(plots)} telek szerepel.')

selected = int(input('3. feladat. Egy tulajdonos adószáma: '))
found = False
for plot in plots:
    if int(plot[0]) == selected: 
        print(f'{plot[1]} {plot[2]}')    
        found = True
if not found: print('Nem szerepel az adatállományban.')

def ado(adosav, adoterulet):
    ado_sum = 0
    if adosav == 'A':
        ado_sum = int(costs[0])*int(adoterulet)
    if adosav == 'B':
        ado_sum = int(costs[1])*int(adoterulet)
    if adosav == 'C':
        ado_sum = int(costs[2])*int(adoterulet)
    if ado_sum < 10000: return 0
    else: return ado_sum

savok = ['A', 'B', 'C']

print('5. feladat')
for sav in savok:
    cost_sum = 0
    plot_sum = 0
    for plot in plots:
        if plot[3] == sav:
            plot_sum += 1
            cost_sum += ado(plot[3], plot[4])
    print(f'{sav} sávba {plot_sum} telek esik, az adó {cost_sum} Ft.')

multiple_streets = {}
for plot in plots:
    # current_street = plot[1]
    # current_ado = plot[3]
    # for plot2 in plots:
    #     if current_street == plot2[1] and current_ado != plot2[3]:
    #         if current_street in multiple_streets:
    #             multiple_streets[current_street].add(plot2[3])
    if plot[1] in multiple_streets:
        multiple_streets[plot[1]].add(plot[3])
    else:
        multiple_streets[plot[1]] = set(plot[3])
            
print('6. feladat. A több sávba sorolt utcák: ')
for street in multiple_streets:
    if len(multiple_streets[street]) > 1:
        print(street)

with open('fizetendo.txt', 'w') as f:
    output = {}
    for plot in plots:
        if plot[0] in output:
            output[plot[0]] += (ado(plot[3], plot[4]))
        else:
            output[plot[0]] = ado(plot[3], plot[4])

    for user in output:
        print(f'{user} {output[user]}', file=f)
        # owner_id = plot[0]
        # price_summed = 0
        # for plot2 in plots:
        #     if plot2[0] == owner_id:
        #         price_summed += ado(plot2[3], plot2[4])
        # print(f'{owner_id} {price_summed}', file=f)