numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 10]

print(numbers)

# Adding Value at the end of the list
numbers.append(11)
print(numbers)

# adding value at a specific index
numbers.insert(0, 0)
print(numbers)

# Removing specific Value from the list
numbers.remove(8)
print(numbers)

# if we try to remove a number that doesn't exist will throw an error
# numbers.remove(12) # will throw an error
# print(numbers)

if 12 in numbers:
    numbers.remove(12)
print("after trying to remove 12", numbers)

# pop() removes the last element and returns it
val = numbers.pop()
print(val)

# index() it used to search and find the index of an element. if value doesn't exit it will throw an error. So we have to check it first

if 7 in numbers:
    idx = numbers.index(7)
    print(idx)
if 18 in numbers:
    idx = numbers.index(18)
    print(idx)