# with open("message.txt", 'w') as file:
#     file.write("Hey there!\n")

# with open("message.txt", 'a') as file:
#     file.write("Hey there!\n")

with open("message.txt", 'r') as file:
    text = file.read()
    print(text)
    print("--------")
    file.seek(1) # moves the cursor at index 1
    print(file.readline())
    print(file.readlines())

