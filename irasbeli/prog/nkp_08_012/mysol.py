import random

# user_csapatnev = input('Adja meg a két csapat nevét! ').split('-')
# user_eredmeny = input('Adja meg az eredményt! ').split(':')
user_csapatnev = ['Pusztakotkodácsi Telkes Gazdák', 'Tálpoharasi Trubadúrok']
user_eredmeny = ['5', '6']

def x12(gól1, gól2): 
   if gól1 > gól2:
       return '1'
   else:
     if gól2 > gól1:
        return '2'
     else:
        return 'X'

csapatok = []
with open('csapatnevek.txt', 'r', encoding='utf8') as f:
    [csapatok.append(line.strip()) for line in f.readlines()]

merkozesek = []
already_played = set()
for i in range(7):
    team_1 = random.choice(csapatok)
    team_2 = random.choice(csapatok)
    found = False
    while team_2 == team_1 and found:
        team_2 = random.choice(csapatok)
    
    if team_1 not in already_played and team_2 not in already_played:
        already_played.add(team_1)
        already_played.add(team_2)
        merkozesek.append({'team_1': team_1, 'team_2': team_2, 'team_1_gol': random.randint(0, 5), 'team_2_gol': random.randint(0, 5)})
        found=True

with open('szelveny.txt', 'w', encoding='utf8') as f:
    for merkozes in merkozesek:
        print(f"{merkozes['team_1']} - {merkozes['team_2']} {merkozes['team_1_gol']}:{merkozes['team_2_gol']} {x12(merkozes['team_1_gol'], merkozes['team_2_gol'])}")