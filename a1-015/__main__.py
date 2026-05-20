name: str = input()
surname: str = input()
age: str = input()

result: str = ""

if len(name) > 5:
    result += name[:2]
    result += surname[-1:]
    result += age[-1:]
else:
    result += name[:1]
    result += age
    result += surname[-1:]

print(result)