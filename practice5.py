while True:
    print("Number 1?");input1 = input()
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
    print("Number 2?");input2 = input()
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

print('%s + %s = %s' % (num1,num2,(num1 + num2)))
print('%s - %s = %s' % (num1,num2,(num1 - num2)))
print('%s * %s = %s' % (num1,num2,(num1 * num2)))
if num1 == 0 and num2 == 0:
    print('0 / 0 = ?')
elif num2 == 0:
    print('%s / 0 = ∞' % (num1))
else:
    print('%s / %s = %s' % (num1,num2,(num1 / num2)))
