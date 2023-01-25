# inform a number and i'll show its multiplication table

while True:
    cn = 0
    table = int(input('Which multiplication table wanna see: '))
    if table < 0:
        print('finished')
        break
    while cn < 10:
        cn += 1
        print(f'{table} x {cn} = {table * cn}')
