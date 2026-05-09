myTk = int(input())
shoePrice = int(input())
shirtPrice = int(input())

if myTk <= 500:
    if (myTk >= shoePrice):
        print("I will buy only a pair of shoes")
    else:
        print("I don't have money to buy shoe")
elif myTk <= 1000:
    if (myTk >= shirtPrice):
        print("I've just bought one shirt")
    else:
        print("don't have money to buy a shirt. I'll buy a pair of shoe instead")
else:
    tkRemain = myTk - shirtPrice
    print(f"I've bought a shirt for {shirtPrice} taka")
    if tkRemain >= 500:
        print(f"I've bought a pair of shoes also for {shoePrice} taka")
    else:
        print("Don't have enough money to buy a pair of shoe")
