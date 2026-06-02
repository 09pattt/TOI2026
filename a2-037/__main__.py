import sys
from collections import deque


def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    q = int(input_data[0].strip())

    emergency_q = deque()
    normal_q = deque()

    for i in range(1, q + 1):
        if i >= len(input_data):
            break
        line = input_data[i].strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]

        if command == 'ARRIVE':
            name = parts[1]
            patient_type = parts[2]

            if patient_type == 'emergency':
                emergency_q.append(name)
            else:
                normal_q.append(name)

        elif command == 'TREAT':
            if emergency_q:
                emergency_q.popleft()
            elif normal_q:
                normal_q.popleft()

        elif command == 'SHOW':
            if not emergency_q and not normal_q:
                print("EMPTY")
            else:
                current_queue = list(emergency_q) + list(normal_q)
                print(" ".join(current_queue))


main()