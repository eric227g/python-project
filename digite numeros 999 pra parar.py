# type random numbers and those will be summed and the amount of numbers typed will be informed (999 to stop)

c = qt = n = 0

while n != 999:
    n = int(input('Number: '))
    if n != 999:
        c += n
        qt += 1
    elif n == 999:
        print('party is over', end='. ')
print(f'you typed {qt} numbers and the sum among these are {c}')