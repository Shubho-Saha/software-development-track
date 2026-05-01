person = {'name': 'shubho', 'age':29, 'uni':'brur'}

print(person)
print(person['name'])
print(person.keys())
print(person.values())
print("-----------")

for key, val in person.items():
    print(key, " : ", val)

numbers = [11, 22, 33, 44, 55, 66, 77]

for idx, val in enumerate(numbers):
    print(idx, " : ", val)