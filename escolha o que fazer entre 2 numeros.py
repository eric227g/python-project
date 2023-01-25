# type 2 numbers and a menu will display to choose what you want to do with them

choice = 0
fn = int(input('1st number: '))  # first number
sn = int(input('2nd number: '))  # second number
while choice != 5:
    choice = int(input("""
    [ 1 ] sum
    [ 2 ] multiply
    [ 3 ] which one is greater
    [ 4 ] new numbers
    [ 5 ] finish program 
    what you wish to do with the informed numbers: """))

    if choice == 1:
        print(f'{fn} + {sn} = {fn + sn}')
    elif choice == 2:
        print(f'{fn} x {sn} = {fn * sn}')
    elif choice == 3:
        if fn > sn:
            print(f'{fn} is greater than {sn}')
        elif fn == sn:
            print(f'{fn} is equals to {sn}')
        else:
            print(f'{sn} is greater than {fn}')
    elif choice == 4:
        fn = int(input('1st number: '))
        sn = int(input('2nd number: '))
    elif choice == 5:
        print('ok then. Hope you enjoyed while it lasted (:')
    else:
        print("Can't you see it's between 1 and 5?!")
