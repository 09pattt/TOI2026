raw: str = input().lower()
target = ['a', 'e', 'i', 'o', 'u']
result: int = 0

for letter in raw:
    if letter in target:
        result += 1

print(result)