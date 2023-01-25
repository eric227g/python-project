# type a number and its factorial will be shown below

f = int(input('Number: '))
c = f
h = 1
while c != 1:
    print(f'{c}', end='')
    h *= c
    c -= 1
    print(' x ' if c > 1 else ' = ', end='')
print(f'{h}')
