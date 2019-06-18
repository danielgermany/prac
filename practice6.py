import datetime

while True:
    print('What is your current age?');input1 = input()
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
    print('At what age do you want to retire?');input2 = input()
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
retireage = num2 - num1
currentDT = datetime.datetime.now()
currentYear = currentDT.year
retireYear = currentYear + retireage
if retireage == 0:
    print('You should retire right now!')
elif retireage < 0:
    print('You are already old enough to retire! You shoudl\'ve retired %s year(s) ago!' % (retireage * -1))
    print('It is %s right now, you should have retired in %s' % (currentYear,retireYear))
else:
    print('You have %s year(s) before you retire' % (retireage))
    print('It is %s right now, so you can retire in %s.' % (currentYear,retireYear))
