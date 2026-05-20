month: int = int(input())
day: int = int(input())

ss: list = ["winter", "spring", "summer", "fall"]
this_ss: int = 0

for r in range(3, 13, 3):
    if month <= r:
        if day >= 21 and month == r:
            print(ss[(this_ss + 1) % len(ss)])
        else:
            print(ss[this_ss])
        break
    this_ss = this_ss + 1