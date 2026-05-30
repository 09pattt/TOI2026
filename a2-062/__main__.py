in1 = input().lower()

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for e in in1:
    if e == 'a':
        vowels['a'] += 1
    elif e == 'e':
        vowels['e'] += 1
    elif e == 'i':
        vowels['i'] += 1
    elif e == 'o':
        vowels['o'] += 1
    elif e == 'u':
        vowels['u'] += 1

if vowels['a']:
    print(f'a: {vowels["a"]}')
if vowels['e']:
    print(f'e: {vowels["e"]}')
if vowels['i']:
    print(f'i: {vowels["i"]}')
if vowels['o']:
    print(f'o: {vowels["o"]}')
if vowels['u']:
    print(f'u: {vowels["u"]}')