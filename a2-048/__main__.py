import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    scores = [int(x) for x in input_data[1:n + 1]]

    student_list = [f"Student{i}" for i in range(1, n + 1)]
    print("Student:", " ".join(student_list))

    if n == 0:
        return

    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / n

    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {average:.1f}")

    print("Students who scored above average:")
    for i in range(n):
        if scores[i] > average:
            print(f"Student {i + 1}")


main()