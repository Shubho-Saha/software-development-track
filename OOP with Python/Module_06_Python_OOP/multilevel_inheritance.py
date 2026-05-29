class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def __repr__(self):
        return f"Vehicle: brand: {self.brand} price: {self.price}"
    
class Bus(Vehicle):
    def __init__(self, brand, price, wheel, seat):
        super().__init__(brand, price)
        self.wheel = wheel
        self.seat = seat
    def __repr__(self):
        return super().__repr__() + f" wheel: {self.wheel} seat: {self.seat}"
    

B1 = Bus("Toyota", 1000000, 4, 40)
print(B1)