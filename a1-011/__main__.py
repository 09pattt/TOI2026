raw: str = input().strip().upper()

result: str = ""
last_char: str = raw[0]
count: int = 1

for i in range(1, len(raw)):
    if raw[i] == last_char:
        count += 1
    else:
        result += f"{count}{last_char}"
        count = 1
        last_char = raw[i]

result += f"{count}{last_char}"

print(result)