# table multiplication

t = int(input('Number you wish to see the multiplication table: '))
for c in range(1, 11):
    print(f'{t} x {c:2} = {c * t}')