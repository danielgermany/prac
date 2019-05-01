def askQuestion():
    print("What question?");ques = int(input())
    return ques

#Questions

def question1(ID):
    if ID == 1:
        print("What is your name?");name = input()
        print("Hello, ", name , ", nice to meet you")
