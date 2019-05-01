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
