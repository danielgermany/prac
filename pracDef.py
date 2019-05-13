def askQuestion():
    print("What question?");ques = int(input())
    return ques

#Questions

def question1(name):
    print("Hello, ", name , ", nice to meet you")

def question2(string):
    amount = len(string)
    print("%s has %s characters." % (string,amount))

def question3(quote,author):
    print('%s says, "%s"' % (author,quote))

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
