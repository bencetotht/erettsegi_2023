import random
szam = random.randint(1, int(input('felso ertek: ')))

user_guess = 0
probalkozasok = 0
while user_guess != szam:
    user_guess = int(input('tipp: '))
    probalkozasok += 1
    if user_guess < szam:
        print(f'nagyobb, probalkozas: {probalkozasok}')
    elif user_guess > szam:
        print(f'kisebb, probalkozas {probalkozasok}')
    if user_guess == -1:
        print(szam)
        break