from function import *
import constant

anotherItem = 1
subtotalAmount = 0

while anotherItem == 1:
    priceItem = checkInput_float("Price of item?")
    amountItem = checkInput("How many of item?")
    anotherItem = checkInput_range("Another item? If so enter 1, if not enter 2",1,2)
    subtotalAmount = subtotalAmount + (priceItem * amountItem)

totalAmount = subtotalAmount * (1 + constant.TAXRATE)

print("""Subtotal: %s
Tax: %s
Total: %s""" % (round(subtotalAmount,2), round(subtotalAmount * constant.TAXRATE,2),round(totalAmount,2)))
