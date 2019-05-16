from pracDef import *

x = askQuestion()

if x == 1:
    print("What is your name?");input = input()
    question1(input)
elif x == 2:
    print("Input?");input = input()
    question2(input)
elif x == 3:
    print("Quote?");input1 = input()
    print("Author?");input2 = input()
    question3(input1,input2)
elif x == 4:
    print("Noun?");input1 = input()
    print("Verb?");input2 = input()
    print("Advjective?");input3 = input()
    print("Adverb?");input4 = input()
    question4(input1,input2,input3,input4)
elif x == 5:
    while True:
        print("Number 1?");input1 = input()
        print("Number 2?");input2 = input()
        try:
            num1 = int(input1)
            if num1 < 0:
                print("You entered a negative number")
                continue

        except ValueError:
            print("You entered a string")
            continue

        try:
            num2 = int(input2)
            if num2 < 0:
                print("You entered a negative number")
                continue
        except ValueError:
            print("You entered a string")
            continue

        question5(num1,num2)

elif x == 6:
    while True:
        print('What is your current age?');input1 = input()
        print('At what age do you want to retire?');input2 = input()
        try:
            num1 = int(input1)
            if num1 < 0:
                print("You entered a negative number")
                continue

        except ValueError:
            print("You entered a string")
            continue

        try:
            num2 = int(input2)
            if num2 < 0:
                print("You entered a negative number")
                continue
        except ValueError:
            print("You entered a string")
            continue
        question6(num1,num2)
elif x == 7:
    stringList = getInputs(True,False,"Hi","hello","twice","hurd")
    Uinput = getInputs(True,False,"Hi","hello","twice","hurd")

    for x in range(4):
        print(stringList[x - 1])
        print(Uinput[x - 1])
