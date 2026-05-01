numbers = {11, 3, 99, 4, 11, 99, 45}

print(numbers)

numbers.add(88)
print(numbers)
numbers.remove(4)
print(numbers)

# will throw an error if the number is not present
# numbers.remove(44)
# print(numbers)

print("discarding 44")
numbers.discard(44)
print(numbers)

# pop() removes a random element and returns it
print(numbers.pop())
print(numbers.pop())

A = {1, 3, 5}
B = {1, 2, 4, 5, 7}

print(A & B)
print(A | B)

print (A - B)
print(B - A)