import sys


def main():
    s = sys.stdin.read().strip().upper()
    if not s:
        return

    n = len(s)
    has_other_chars = False
    for char in s:
        if char in ('R', 'A', 'B'):
            has_other_chars = True
            break

    if not has_other_chars:
        print(f"unknown {n}")
        return
    for i in range(n):
        char = s[i]
        if char == 'R':
            if i + 1 >= n or s[i + 1] != 'A':
                print(f"no {i + 1 if i + 1 < n else i}")
                return
        elif char == 'B':
            if i + 1 >= n or s[i + 1] not in ('I', 'T'):
                print(f"no {i + 1}")
                return
        elif char == 'A':
            if i == 0 or s[i - 1] not in ('R', 'A'):
                print(f"no {i}")
                return
        elif char not in ('I', 'T'):
            print(f"no {i}")
            return
    max_a = 0
    current_a = 0
    for char in s:
        if char == 'A':
            current_a += 1
            if current_a > max_a:
                max_a = current_a
        else:
            current_a = 0

    print(f"yes {max_a}")


main()