n = int(input())
vowels = 'AEIOU'
count = 0

for i in range(n):
    letter = input()
    if letter in vowels:
        count += 1

print(count)