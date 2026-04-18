def addNums(num1, num2):
    result = num1 + num2
    return result

total = addNums(10, 20)
print("Total = ", total)

def fun(num1, num2, *nums):
    print("first two numbers: ", num1, num2)
    sum = num1 + num2
    for num in nums:
        print(num)
        sum += num
    return sum

res = fun(5, 10, 20, 30, 40)
print("final ", "result ", res, " !")
    
