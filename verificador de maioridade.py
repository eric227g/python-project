# type 7 different year and i'll show how many are above and under 21 yo

from datetime import date

ctyear = date.today().year
ag = 0  # above age
ug = 0  # underage
for c in range(7):
    year_birth = int(input('year: '))
    if ctyear - year_birth >= 21:
        ag += 1
    else:
        ug += 1
print(f'there are {ag} people above age\nand {ug} under age')