import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    total = n * n
    a = input_data[1 : 1 + total]
    b = input_data[1 + total : 1 + (2 * total)]

    for i in range(n):
        result = []
        for j in range(n):
            idx = (i * n) + j
            val = int(a[idx]) + int(b[idx])
            result.append(str(val))
        print(" ".join(result))

main()