year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 or year == 1500:
    print("yes")
else:
    print("no")