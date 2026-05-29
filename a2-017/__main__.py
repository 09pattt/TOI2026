meal = {
    "S": {
        "R": 60,
        "T": 80
    },
    "M": {
        "R": 80,
        "T": 100
    },
    "L": {
        "R": 100,
        "T": 120
    }
}

toppings = {
    "P": 15,
    "E": 10
}

in1 = input().split()
in2 = input().split()
result = 0

size = in1[0]
menu = in1[1]
topping = in2[0]

result += meal[size][menu]
if not topping == "N":
    topping_qtt = int(in2[1])
    result += topping_qtt * toppings[topping]

print(result)