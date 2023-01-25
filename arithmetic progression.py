# type the amount of numbers you wanna see of an AP (arithmetic progression)

print(30 * "=")
print("10 terms of AP")
print(30 * "=")

ft = int(input('first term: '))
ss = int(input('difference: '))
tenth = ft + (10 - 1) * ss
for c in range(ft, tenth + ss, ss):
    print(c, end=' -> ')
print('END')