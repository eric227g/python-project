# sum 6 even numbers, if it's odd, don't consider it

es = 0
ct = 0
for c in range(1, 7):
    e = int(input(f'number {c}: '))
    if e % 2 == 0:
        es += e
        ct += 1
print(f'you informed {ct} numbers and the sum among them is: {es}')
