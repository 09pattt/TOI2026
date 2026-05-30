raw = input()
highest_count = 0

count = 0
is_counting = False
for e in raw:
    if is_counting:
        if e in "Uu":
            count += 1
            if count > highest_count:
                highest_count = count
        else:
            count = 0
            is_counting = False
    elif e in "Bb":
        count = 0
        is_counting = True

if highest_count >= 2:
    print(f"Yes {highest_count}")
else:
    result = ""
    if "B" in raw or "b" in raw:
        found_b = False
        for e in raw:
            if found_b:
                result += "U"
            else:
                if e in "Bb":
                    found_b = True
                result += e
        print(result)
    else:
        while len(result) < len(raw):
            result += "BUU"
        print(result[:len(raw)])