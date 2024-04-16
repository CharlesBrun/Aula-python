class Bike:
    def __init__(self, color, model, year, price):
        self.color = color
        self.model = model
        self.year = year
        self.price = price

    def honk(self):
        print("Plim plim...")

    def stop(self):
        print("Stoped...")

    def run(self):
        print("Runing...")

    def __str__(self) -> str:
        return f"Bike: {self.color}, {self.model}, {self.year} and ${self.price}"

caloi = Bike("red", "caloi", 2024, 600)

print(caloi)