class Warehouse:
    def __init__(self):

        self.inventory = {}

        self.logs = []

    def add(self, name, qty):
        self.inventory[name] = self.inventory.get(name, 0) + qty

    def remove(self, name, qty):
        current_qty = self.inventory.get(name, 0)
        if qty > current_qty:
            self.logs.append(f"Not enough stock for {name}")
            new_qty = 0
        else:
            new_qty = current_qty - qty

        if new_qty <= 0:
            if name in self.inventory:
                self.inventory.pop(name, None)
        else:
            self.inventory[name] = new_qty

    def check(self):

        low_stock = sorted([n for n, q in self.inventory.items() if q < 5])
        if low_stock:
            self.logs.extend(low_stock)
        else:
            self.logs.append("All stocks are sufficient")

    def report(self):

        for name in sorted(self.inventory.keys()):
            self.logs.append(f"{name}: {self.inventory[name]}")

    def show_results(self):
        if self.logs:
            print("\n".join(self.logs))


def start_system():
    wh = Warehouse()
    commands = []

    while True:
        try:
            line = input().strip()
            if not line: continue
            commands.append(line)
            if line == "END": break
        except EOFError:
            break

    for cmd in commands:
        p = cmd.split()
        if p[0] == "ADD":    wh.add(p[1], int(p[2]))
        if p[0] == "REMOVE": wh.remove(p[1], int(p[2]))
        if p[0] == "CHECK":  wh.check()
        if p[0] == "REPORT": wh.report()
        if p[0] == "END":    break

    wh.show_results()


start_system()