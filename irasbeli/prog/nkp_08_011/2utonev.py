data_2011 = []
data_2021 = []
with open('top100utonev_2011.txt') as f:
    for line in f.readlines():
        insert_line = line.strip().split()
        data_2011.append({'name': insert_line[0], 'num': int(insert_line[1]), 'nem': insert_line[2], 'evszam': insert_line[3]})
with open('top100utonev_2021.txt') as f:
    for line in f.readlines():
        insert_line = line.strip().split()
        data_2021.append({'name': insert_line[0], 'num': int(insert_line[1]), 'nem': insert_line[2], 'evszam': insert_line[3]})

# kozos_nevek = []
# [kozos_nevek.append(name) for name in nevek_2011 if name in nevek_2021]

rendezett_2011 = sorted(data_2011, key=lambda x: x['num'], reverse=True)
returnarray_2011 = []
for data in rendezett_2011:
    if data['nem'] == 'N': returnarray_2011.append(data)
rendezett_2021 = sorted(data_2021, key=lambda x: x['num'], reverse=True)
returnarray_2021 = []
for data in rendezett_2021:
    if data['nem'] == 'N': returnarray_2021.append(data)

already_processed = []
for data in returnarray_2011:
    for data2 in returnarray_2021:
        if data['name'] == data2['name']:
            already_processed.append({'name': data['name'], 'no_2011': returnarray_2021.index(data2) + 1, 'no_2022': returnarray_2011.index(data) + 1, 'valtozas': (returnarray_2021.index(data2) + 1) - (returnarray_2011.index(data) + 1)})
print(already_processed)