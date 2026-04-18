def all_sum(num1, num2, *nums, **knums):
    print(f"single numbers: {num1} and {num2}")
    print(f"args numbers: ", end=" ")
    for n in nums:
        print(n, end=" ")
    print()
    for key, val in knums.items():
        # print(key, " : ", val, end=" ")
        print(f"{key} : {val}", end=" ")


all_sum(1, 2, 3, 4, five = 5, six =6)