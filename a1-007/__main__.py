target: list = ["a", "e", "i", "o", "u"]

letter: str = input().lower()

if letter in target:
    print("yes")
else:
    print("no")