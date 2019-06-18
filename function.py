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
