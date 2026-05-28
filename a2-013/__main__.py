beverage_data = {
    "R": {
        "s1": 12,
        "s2": 18,
        "s3": 25
    },
    "T": {
        "s1": 15,
        "s2": 20,
        "s3": 30
    },
    "M": {
        "s1": 10,
        "s2": 15,
        "s3": 20
    }
}

topping_data = {
    "H": 5,
    "O": 3,
    "J": 2
}

in1 = input().split()
in2 = input().split()

topping = in1[0]
topping_qtt = int(in1[1])

beverage = in2[0]
sweetness = int(in2[1])
beverage_qtt = int(in2[2])

result = 0

result += beverage_data[beverage][f"s{sweetness}"] * beverage_qtt
result += topping_data[topping] * topping_qtt

print(result)