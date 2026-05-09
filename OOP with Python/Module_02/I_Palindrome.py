number = input()
# print(number)

sz = len(number)
# print(sz)

left = 0; right = sz-1
flag = True
while (left < right):
    if(number[left] != number[right]):
        flag = False
    left += 1
    right -= 1

Seen = False
for i in range (sz-1, -1, -1):
    if(number[i] != '0'):
        Seen = True
    if Seen:
        print(number[i], end="")
    else:
        if (number[i] != '0'):
            print(number[i], end="")
print()
if flag:
    print("YES")
else:
    print("NO")
