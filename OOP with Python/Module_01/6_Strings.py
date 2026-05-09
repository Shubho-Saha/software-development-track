name = "Mrinmoy Saha ShubhO"

print(name[0], name[-1])
print(name[1:])
print(name[:7])

msg = f"Hi my name is {name}"
print(msg)

msg2 = msg.upper();
print(msg2)
print(msg.title())
flag = msg.find("Saha")
print(f"flag: {flag}")

print("moy" in msg)