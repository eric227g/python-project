# odds and evens, we'll play it until the user(you) lose
from random import randint
r = randint(0, 10)
print(15 * '=-')
print("LET'S PLAY ODDS AND EVENS")
print(15 * '=-')
counter = 0

while True:
    n = int(input('type a value: '))
    c = str(input('even or odd? [E/O] ')).strip().lower()[0]
    if c not in 'e' and c not in 'o':
        print("only e's and o's")
    else:
        result = n + r
        print(f'you chose {n} and the computer {r}. Total is {result} ', end='')
        if c == 'e':
            if result % 2 == 0:
                print('EVEN')
                print('you won!')
                counter += 1
            else:
                print("\nbetter luck next time... you lost :'( ")
                break
        if c == 'o':
            if result % 2 == 1:
                print('ODD')
                print('you won!')
                counter += 1
            else:
                print("\nbetter luck next time... you lost :'( ")
                break
print(f'you won {counter} times')
