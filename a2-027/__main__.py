dataset = []

in1 = int(input())

while len(dataset) < in1:
    dataset.append(int(input()))

dataset.sort(reverse=True)

top = dataset[0]
count = 0

for e in dataset:
    if e == top:
        count += 1

print(top)
print(count)