from function import *

euroAmount = checkInput_float("How many euros?")
exhangeRate = checkInput_float("What is the exhange rate?")
print("%s euros at an exhange rate of %s is %s U.S. dollars." % ((euroAmount,exhangeRate,round(((euroAmount * exhangeRate)/100),2))))
