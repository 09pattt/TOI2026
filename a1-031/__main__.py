raw: str = input()
lenght: int = len(raw)
fraction: int = lenght % 3
result: str = ""

for i in range(0, fraction):
    result += raw[i]

if not fraction == 0:
    result += ','
count: int = 0

for i in range(fraction, len(raw)):
    count += 1
    result += raw[i]
    if count % 3 == 0 and not i == len(raw) - 1:
        result += ','

print(result)