class Family:
    Family_Name = "Saha"
    fam_cart = []
    def __init__(self, member):
        self.member = member
        self.cart = []

    def add_to_cart(self, *items):
        for i in items:
            self.cart.append(i)
    def add_to_famCart(self, *items):
        for i in items:
            self.fam_cart.append(i)

Shubho = Family("Shubho Saha")
Monimoy = Family("Monimoy")

Shubho.add_to_cart("shoes", "belt", "perfume")
Shubho.add_to_famCart("tomato", "sugar")

Monimoy.add_to_cart("babyoil", "banana", "medcine")
Monimoy.add_to_famCart("chili", "Soyabin", "Fish")

print(Shubho.Family_Name)
print(Shubho.fam_cart)
print(Shubho.cart)