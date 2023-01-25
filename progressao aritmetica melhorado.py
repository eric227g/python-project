# update the arithmetic progression to if the user wants to see more terms

print("AP Generator")
print("-=" * 10)
it = int(input("Initial term: "))
cd = int(input("Common difference: "))
term = it
cont = 1
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print(f"{term} - ", end="")
        term += cd
        cont += 1
    print("PAUSE")
    more = int(input("How many more terms you wanna see? "))
print(f"Progression finished with {total} terms shown.")
