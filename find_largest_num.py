arr = [10,621,839,774,965,564,472,638,129,610]


num = 0


for number in arr:
    if number > num:
        num = number
        print("Num so far: ", num)

print("Largest", num)