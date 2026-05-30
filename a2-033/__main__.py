import sys


def parse_and_validate(time_str):
    if '.' not in time_str:
        return -1

    try:
        parts = time_str.split('.')
        if len(parts) != 2:
            return -1

        hours = int(parts[0])
        minutes = int(parts[1])
        if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
            return -1
        if len(parts[1]) != 2:
            return -1
        return (hours * 60) + minutes
    except ValueError:
        return -1


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        print("ERROR")
        return

    in_str = input_data[0]
    out_str = input_data[1]
    time_in = parse_and_validate(in_str)
    time_out = parse_and_validate(out_str)

    if time_in == -1 or time_out == -1:
        print("ERROR")
        return
    if time_out <= time_in:
        print("ERROR")
        return
    duration_mins = time_out - time_in
    if duration_mins < 15:
        print("FREE")
        return
    hours_charged = duration_mins // 60
    rem_mins = duration_mins % 60
    if rem_mins > 0:
        hours_charged += 1
    if hours_charged == 1:
        fee = 25
    elif hours_charged == 2:
        fee = 50
    elif hours_charged == 3:
        fee = 80
    elif hours_charged == 4:
        fee = 110
    elif hours_charged == 5:
        fee = 145
    elif hours_charged == 6:
        fee = 180
    else:
        fee = 250

    print(fee)


solve()