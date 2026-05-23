card = input().upper()

names = {'A': 'ace', 'J': 'jack', 'Q': 'queen', 'K': 'king'}
groups = {'D': 'diamonds', 'C': 'clubs', 'S': 'spades', 'H': 'hearts'}

front = card[:-1]
back = card[-1]

name = names.get(front, front)
group = groups.get(back)

print(f"{name} of {group}")