def checkInput(string):
    while True:
        print(string)
        userInput = input()
        try:
            num = int(userInput)
            if num < 0:
                print("You entered a negative number")
                continue
            else:
                return num
                break
        except ValueError:
            print("You entered a string")
            continue
def checkInput_range(string,range1,range2):
    while True:
        print(string)
        userInput = input()
        try:
            num = int(userInput)
            if num < 0:
                print("You entered a negative number")
                continue
            elif range1 <= num <= range2:
                return num
                break
            else:
                print("You entered a value outside the range")
                continue
        except ValueError:
            print("You entered a string")
            continue
def checkInput_float(string):
        while True:
            print(string)
            userInput = input()
            try:
                num = float(userInput)
                if num < 0:
                    print("You entered a negative number")
                    continue
                else:
                    return num
                    break
            except ValueError:
                print("You entered a string")
                continue
