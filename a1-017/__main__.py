class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

y1: int = int(input())
m1: int = int(input())
d1: int = int(input())
y2: int = int(input())
m2: int = int(input())
d2: int = int(input())

b1 = Birthday(y1, m1, d1)
b2 = Birthday(y2, m2, d2)

if b1.year < b2.year:
    print(1)
elif b1.year == b2.year:
    if b1.month < b2.month:
        print(1)
    elif b1.month == b2.month:
        if b1.day < b2.day:
            print(1)
        elif b1.day == b2.day:
            print(0)
        else:
            print(2)
    else:
        print(2)
else:
    print(2)