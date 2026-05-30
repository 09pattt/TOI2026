input_list = []
count = 0

while True:
    in1 = int(input())

    if count >= 3:
        if in1 == 0:
            break
        elif in1 == 1:
            print('Original order:', end='')
            for e in input_list:
                print(f' {e}', end='')
            break
        elif in1 == 2:
            print('Descending order:', end='')
            input_list.sort(reverse=True)
            for e in input_list:
                print(f' {e}', end='')
            break
        elif in1 == 3:
            print('Ascending order:', end='')
            input_list.sort()
            for e in input_list:
                print(f' {e}', end='')
            break

    count += 1
    input_list.append(in1)
    print(f'Input number {count} stored.')