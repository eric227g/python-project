# fibonacci sequence

fb = int(input('fibonacci sequence: '))
n1, n2 = 0, 1
count = 0
while count < fb:
    print(n1, end=' - ')
    number = n1 + n2
    n1 = n2
    n2 = number
    count += 1
print('END')