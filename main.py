class Machine:
    def __init__(self, productivity, cost, avg_part_price):
        self.productivity = productivity
        self.cost = cost
        self.avg_part_price = avg_part_price

    def breakeven_parts(self):
        return self.cost / self.avg_part_price

    def __add__(self, other):
        if isinstance(other, Machine):
            return self.cost + other.cost
        return NotImplemented

class MillingMachine(Machine):
    def __init__(self, productivity, cost, avg_part_price, spindle_speed):
        super().__init__(productivity, cost, avg_part_price)
        self.spindle_speed = spindle_speed

    def payback_time(self, fixed_price):
        return self.cost / (self.productivity * fixed_price)

class CNCMachine(Machine):
    def __init__(self, productivity, cost, avg_part_price, precision_level):
        super().__init__(productivity, cost, avg_part_price)
        self.precision_level = precision_level

    def payback_time(self, fixed_price):
        return self.cost / (self.productivity * fixed_price)

# пример использования:
if __name__ == "__main__":
    machine1 = MillingMachine(50, 20000, 10, 1200)
    machine2 = CNCMachine(80, 50000, 15, 0.01)

    print("Milling Machine breakeven parts:", machine1.breakeven_parts())
    print("CNC Machine breakeven parts:", machine2.breakeven_parts())

    print("Milling Machine payback time:", machine1.payback_time(12), "hours")
    print("CNC Machine payback time:", machine2.payback_time(20), "hours")

    total_cost = machine1 + machine2
    print("Total cost of both machines:", total_cost)

