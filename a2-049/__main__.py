import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    mod = (2 ** 15) + 9
    a = []
    b = []

    idx = 0
    for i in range(3):
        row = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        a.append(row)
        idx += 3

    for i in range(3):
        row = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        b.append(row)
        idx += 3
    c = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            current_sum = 0
            for k in range(3):
                current_sum += a[i][k] * b[k][j]
            c[i][j] = (current_sum % mod + mod) % mod
    for i in range(3):
        print(" ".join(str(c[i][j]) for j in range(3)))


main()