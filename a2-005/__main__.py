def main():
    w, h, m, n = map(int, input().split())

    x_cuts = [0] + list(map(int, input().split())) + [w]
    y_cuts = [0] + list(map(int, input().split())) + [h]
    dx = []
    for i in range(1, len(x_cuts)):
        dx.append(x_cuts[i] - x_cuts[i - 1])

    dy = []
    for i in range(1, len(y_cuts)):
        dy.append(y_cuts[i] - y_cuts[i - 1])
    dx.sort(reverse=True)
    dy.sort(reverse=True)

    largest_1 = dx[0] * dy[0]
    largest_2 = max(dx[1] * dy[0], dx[0] * dy[1])

    print(f"{largest_1} {largest_2}")


main()