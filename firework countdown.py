# firework countdown

from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'\033[31mBOM BOM POOOW{emojize(":fireworks:")}'
      f'{emojize(":partying_face:")}'
      f'{emojize(":party_popper:")}'
      f'\033[m!!!!')