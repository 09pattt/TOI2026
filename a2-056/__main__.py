n = int(input())
items = list(map(int, input().split()))

result = sorted([x for x in items if items.count(x) == 1])

print(*result)