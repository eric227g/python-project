# ask for a person's gender and I going to inform if it's valid or not
c = 'S'
while c == 'S':
    s = str(input('your gender [M/F]: '))
    if s.lower() == 'm' or s.lower() == 'f':
        if s.lower() == 'm':
            print('male')
        else:
            print('female')
        c = ''
    else:
        print('idk')
print('well done')

