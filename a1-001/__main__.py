def greeting(_name: str, _surname: str) -> str:
    return f"Hello {_name} {_surname}"

def alias(_name: str, _surname: str) -> str:
    _name_alias = _name[:2]
    _surname_alias = _surname[:2]
    return _name_alias + _surname_alias

name: str = input()
surname: str = input()

print(greeting(name, surname))
print(alias(name, surname))