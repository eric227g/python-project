# sum all odd numbers multiple of 3 between 1 and 500

so: int = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        so += c
print(f'the result of all {cont} numbers summed is {so}')
