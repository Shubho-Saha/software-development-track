is_raining = False
isWeekend = True

if is_raining and isWeekend:
    print("No chance going office")
elif is_raining or isWeekend:
    print("I'll try boss")

print(type(is_raining))

workDay = not isWeekend
print(workDay)