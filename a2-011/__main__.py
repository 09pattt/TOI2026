raw = input().split()
result = []

for e in raw:
    if not e in result:
        result.append(e)

for e in result:
    print(e + " ", end="")