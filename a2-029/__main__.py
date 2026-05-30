import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    for r in range(n):
        row_output = []
        for c in range(r + 1):
            if c == 0 or r == n - 1 or r == c:
                row_output.append("0")
            else:
                row_output.append("1")
        print(" ".join(row_output))


main()