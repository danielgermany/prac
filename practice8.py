from function import *

amountPeople = checkInput("How many people?")
amountPizza = checkInput("How many pizzas are there?")
amountSlices = checkInput("How many slices in a pizza?")

print("There are %s people with %s pizzas." % (amountPeople,amountPizza))
print("Each person gets %s pieces of pizza." % round((amountPizza * amountSlices) / amountPeople))
print("There are %s leftover slices" % ((amountPizza * amountSlices) % amountPeople))
