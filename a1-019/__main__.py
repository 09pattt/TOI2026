num1 = input()
num2 = input()
num3 = input()

nums = [num1, num2, num3]
highest: int = 0

for p in nums:
    count = 0
    for q in nums:
        if p == q:
            count += 1
    if count > highest:
        highest = count

if highest == 1:
    print("all different")
elif highest == 2:
    print("neither")
elif highest == 3:
    print("all the same")
else:
    raise Exception("ซวยแล้วน้อง")