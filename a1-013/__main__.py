pass_char: str = "H"
pass_digits: str = "4567"
char_valid: bool = False
digits_valid: bool = False

entered_char: str = input()
entered_digits: str = input()

if entered_char == pass_char:
    char_valid = True
if entered_digits == pass_digits:
    digits_valid = True

if char_valid and digits_valid:
    print("safe unlocked")
elif char_valid and not digits_valid:
    print("safe locked - change digit")
elif not char_valid and digits_valid:
    print("safe locked - change char")
elif not char_valid and not digits_valid:
    print("safe locked")