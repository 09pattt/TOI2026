raw = input()
result = ""

first_comma = len(raw) % 3
if first_comma == 0:
    first_comma = 3

for i in range(len(raw)):
    result += raw[i]
    if (i + 1) % 3 == first_comma % 3 and i < len(raw) - 1:
        result += ","

print(result)