# type number, i'll check if it is a prime number or not

num = int(input("Enter a number: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(c, end=" ")
print(f"\n\033[mThe number {num} was divided {tot} times")
if tot == 2:
    print("That's why it IS PRIME")
else:
    print("That's why it IS NOT PRIME")