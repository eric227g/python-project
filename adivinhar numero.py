# guess the number until you get it right

from random import randint
rn = randint(0, 1)
tg = 1
print("I'm your machine... i thought of a number between 0 and 10.")
gn = int(input('What number have i thought of: '))
while gn != rn:
    if gn == rn:
        print('ok')
    else:
        if rn > gn:
            gn = int(input('Lil more... Guess again: '))
        else:
            gn = int(input('lil less... Guess again: '))
    tg += 1
print(f'Good guessing! you needed {tg} times to get it right')
