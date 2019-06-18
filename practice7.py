import practice7_constant

while True:
    print('What is the length of the room in feet?')
    input1 = input()
    try:
        num1 = int(input1)
        if num1 < 0:
            print("You entered a negative number")
            continue
        else:
            break
    except ValueError:
        print("You entered a string")
        continue
while True:
    print('What is the width of the room in feet?')
    input2 = input()
    try:
        num2 = int(input2)
        if num2 < 0:
            print("You entered a negative number")
            continue
        else:
            break
    except ValueError:
        print("You entered a string")
        continue

print("You entered dimensions of %s feet by %s feet" % (num1,num2))
print("The area is %s square feet and %s square meter" % ((num1 * num2),round((num1 * num2) * practice7_constant.FEET_TO_METER,4)))
