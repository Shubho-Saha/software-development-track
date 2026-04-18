balance = 500

def buyItem(item, price):
    # To use global variable we must declare it inside the function if we modify the global variable
    global balance
    # Local Variable
    # balance = 1000
    print(f"before buying balance: {balance}")
    balance = balance - price
    print(f"after buying shirt balance: {balance}")


buyItem('shirt', 200)