in1 = input().split()
price = int(input())

width = int(in1[0])
length = int(in1[1])
layer = int(in1[2])

perimeter = 2 * (width + length)
net = perimeter * layer
print(net)
expenses = net * price
print(expenses)