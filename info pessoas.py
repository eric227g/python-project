"""ask name, age, and gender, and show the average age,
who's the oldest man's name
and how many women are less than 21 yo"""

anage = 0
highest = 0
chname = ""
sum = 0

for g in range(1, 5):
    print(f"{g} person's info")
    name = str(input("What's your name: "))
    age = int(input("Inform your age here please: "))
    sx = str(input("Inform your gender here: ")).strip()
    if age > 1:
        anage += age
    if age > highest and sx.strip().lower()[:4] == "male":
        highest = age
        chname = name
    if age <= 20 and sx.strip().lower()[:6] == "female":
       sum += 1

print(f"The average age among the people mentioned is {int(anage / 4)}")
print(f"The oldest man is {chname.capitalize()} and he is {highest} years old.")
print(f"{sum} female people are under 20 years old.")
