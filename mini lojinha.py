""" read many product's name and prices. System should ask
if the customer wants to continue. At the end, show:
a) how much was spent
b) how many product costs more than 1000$
c) the cheapest product's name"""

pot = tot = lwprice = count = cheap =0
while True:
    name = str(input("product's name: "))
    pric = float(input('price: $'))
    count += 1
    tot += pric
    if pric > 1000:
        pot += 1
    if count == 1 or pric < lwprice:
        lwprice = pric
        cheap = name
    chce = str(input('wish to continue? [Y/N] ')).strip().lower()[0]
    while chce not in 'yn':
        chce = str(input('wish to continue? [Y/N] '))
    if chce == 'n':
        break
print(f'total spent was ${tot}\n{pot} products cost more than 1000 dollars')
print(f'the lowest product is {cheap} which costs ${lwprice}')
