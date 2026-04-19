def addNum(*nums):
    sum = 0; mul = 1
    for n in nums:
        sum += n
        mul *= n
    return sum, mul
if __name__ == "__main__":
    print(addNum(5, 10))
    [sum, mul] = addNum(10, 20)
    print(f"Sum: {sum} and Mul: {mul}")
