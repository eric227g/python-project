"""ATM simulator
ask how much the user wants to withdraw
and the system will inform how many ballots
of each value will be given."""

value = int(input('withdrawal value: $'))
total = value
ball = 50
ballamnt = 0
while True:
    if total >= ball:
        total -= ball
        ballamnt += 1
    else:
        if ballamnt > 0:
            print(f'{ballamnt} ballots of ${ball}')
        if ball == 50:
            ball = 20
        elif ball == 20:
            ball = 10
        elif ball == 10:
            ball = 1
        ballamnt = 0
        if total == 0:
            break
