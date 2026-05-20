import sys


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    trees = int(input_data[0])

    height = [int(x) for x in input_data[1:]]

    if trees == 1:
        print(1)
        return

    count = 0

    if height[0] > height[1]:
        count += 1

    for i in range(1, trees - 1):
        if height[i] > height[i - 1] and height[i] > height[i + 1]:
            count += 1

    if height[-1] > height[-2]:
        count += 1

    print(count)


solve()