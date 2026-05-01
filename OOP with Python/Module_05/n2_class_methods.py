class Calculator:
    brand = "Casio"
    price = 1200

    def add(self, num1, num2):
        return num1+num2
    
    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        return n1/n2

cal = Calculator()

print(cal)
print(cal.brand)
print(cal.add(10, 20))
print(cal.sub(30, 15))
print(cal.mul(5, 8))
print(cal.div(5, 2))