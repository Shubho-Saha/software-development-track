class Vehicle:
    
    def __init__(self, types, brand, price):
        self.types = types
        self.brand = brand
        self.price = price
    
    def description(self):
        text = f"This is a {self.types} of {self.brand} brand and it's price is {self.price}"
        print(text)

bike = Vehicle("Motorcycle", "Yamaha", 400000)
print(bike)
print(bike.brand)
bike.description()
        