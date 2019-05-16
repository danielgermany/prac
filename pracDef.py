import datetime

def askQuestion():
    print("What question?");ques = int(input())
    return ques

def getInputs(TypeInt,AllowNegative,*string):
    stringList = []
    stringLen = len(string)
    print(stringLen)

    for arg in string:
        i = stringLen - 1
        stringList.insert(i,arg)
        i -= 1
    if TypeInt == True:
        Uinput = []
        for n in range(stringLen):
            print(stringList[n]);userInput = input()
            Uinput.insert(n - 1,userInput)
            try:
                num1 = int(Uinput[n - 1])
                if AllowNegative == False:
                    if num1 < 0:
                        print("You entered a negative number")

            except ValueError:
                print("You entered a string")
    elif TypeInt == False:
        for n in range(stringLen):
            print(stringList[n]);userInput = input()
            Uinput.insert(n - 1,userInput)

    return stringList,Uinput

#Questions

def question1(name):
    print("Hello, ", name , ", nice to meet you")

def question2(string):
    amount = len(string)
    print("%s has %s characters." % (string,amount))

def question3(quote,author):
    print('%s says, "%s".' % (author,quote))

def question4(noun,verb,adj,adverb):
    print('Do you %s your %s %s %s ?' % (verb,adj,noun,adverb))

def question5(number1,number2):
    print('%s + %s = %s' % (number1,number2,(number1 + number2)))
    print('%s - %s = %s' % (number1,number2,(number1 - number2)))
    print('%s * %s = %s' % (number1,number2,(number1 * number2)))
    if number1 == 0 and number2 == 0:
        print('0 / 0 = ?')
    elif number2 == 0:
        print('%s / 0 = ∞' % (number1))
    else:
        print('%s / %s = %s' % (number1,number2,(number1 / number2)))

def question6(year1,year2):
    retireage = year2 - year1
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
