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
