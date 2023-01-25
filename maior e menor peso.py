# ask 5 people's weight, the lowest and highest weight will be displayed

hw = 0  # highest weight
lw = 0  # lowest weight 
for c in range(5):
    weight = float(input("Whats your weight: "))
    if c == 0:
        hw = weight
        lw = weight
    else:
        if weight > hw:
            hw = weight
        if weight < lw:
            lw = weight
print(f"The highest weight is {hw}")
print(f"The lowest weight is {lw}")
