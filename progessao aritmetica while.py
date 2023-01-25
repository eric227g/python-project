# arithmetic progression

it = int(input('initial term: '))
cd = int(input('common difference: '))
n = 0
while n < 10:
    print(it, end=' - ')
    it += cd
    n += 1
print('END')
