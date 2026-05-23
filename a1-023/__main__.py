deg: int = int(input())
unit: str = input()

if unit is "C":
    if deg > 0:
        if deg > 100:
            print("gas")
        else:
            print("liquid")
    else:
        print("solid")
else:
    if deg > 32:
        if deg > 212:
            print("gas")
        else:
            print("liquid")
    else:
        print("solid")