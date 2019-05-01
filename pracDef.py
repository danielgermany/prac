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
