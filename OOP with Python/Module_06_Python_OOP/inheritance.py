class Gadget:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class Laptop(Gadget):
    def __init__(self, brand, price, ram, rom):
        super().__init__( brand, price)
        self.ram = ram
        self.rom = rom
    def __repr__(self):
        return f"Laptop brand: {self.brand} price: {self.price} ram: {self.ram}"
    

class Phone(Gadget):
    def __init__(self,brand, price, color, camera):
        super().__init__( brand, price)
        self.color = color
        self.camera = camera
    def __repr__(self):
        return f"Phone brand: {self.brand} price: {self.price} color: {self.color}"

lp1 = Laptop("asus", 770000, 8, 256)
lp2 = Laptop("Hp", 880000, 8, 512)

ph1 = Phone("Samsung", 51000, "Golden", 3)

print(lp1)
print(ph1)
        