# type numbers, at the end the average, the lowest and greatest numbers will be shown

r = "y"
c = q = big = minor = 0
while r in "yY":
    n = int(input("Number: "))
    r = str(input("keep going? [Y / N] ")).lower().strip()[0]
    c += n
    q += 1
    if q == 1:
        big = minor = n
    else:
        if n > big:
            big = n
        elif n < minor:
            minor = n
print(f"""You typed {q} numbers & the average is {c/q},
the biggest number is {big} and the smallest is {minor}""")