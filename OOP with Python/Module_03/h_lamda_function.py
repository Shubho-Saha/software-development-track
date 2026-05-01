doubled = lambda x : x *2
sum = lambda a, b: a+b

d = doubled(11)
print(d)
print(sum(3, 9))

numbers = [11, 22, 33, 20, 40, 50, 99]

doubleIt = map(doubled, numbers)

print(list(doubleIt))

students = [
    {'name': 'Henry', 'age': 15}, 
    {'name': 'tom', 'age': 16}, 
    {'name': 'Evan', 'age': 17}, 
    {'name': 'Rohan', 'age': 18}, 
    {'name': 'Rajib', 'age': 20}, 
]

res = filter(lambda std : std['age'] % 2 == 0, students)

print(list(res))


