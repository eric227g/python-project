# type numbers until you type 999 and show the sum among the numbers and how many were typed

s = c = 0
while True:
    n = int(input("number here (999 to stop): "))
    if n == 999:
        break
    c += 1
    s += n
print(f'the sum among {c} numbers is {s}!')