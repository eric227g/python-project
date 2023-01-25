""" read many people's age and sex. For each person registered,
system should ask if he/she wants to continue. At the end, show:
a) how many are overage
b) how many men registered
c) how many women are under 20 yo"""

print("""
-------------------------
    PEOPLE REGISTRATION
-------------------------""")
fs = ms = abve = 0
while True:
    age = int(input('age: '))
    if age >= 18:
        abve += 1
    sex = str(input('sex: [M / F]: ')).strip().lower()[0]
    if sex == 'f' and age < 20:
        fs += 1
    elif sex == 'm':
        ms += 1
    while sex not in 'mf':
        sex = str(input('sex: [M / F]: ')).strip().lower()[0]
        if sex == 'f':
            fs += 1
        elif sex == 'm':
            ms += 1
    print(25 * '-')
    cc = str(input('wish to continue? [Y/N] ')).strip().lower()[0]
    while cc not in 'yn':
        cc = str(input('wish to continue? [Y/N] ')).strip().lower()[0]
    if cc == 'n':
        break

print(f'People above 18: {abve}\nthere are {ms} men registered')
print(f'there are {fs} women are under 20yo')
