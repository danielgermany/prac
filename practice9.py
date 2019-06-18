from function import *
import constant

length = checkInput("What is the length?")
width = checkInput("What is the width?")

sqArea = length * width
amountPaint = sqArea / constant.SQUARE_FEET_TO_GALLON

if amountPaint == int(amountPaint):
    pass
else:
    amountPaint += 1
    rounded_amountPaint= int(amountPaint)

print("You will need to buy %s gallons of paint to cover %s square feet." % (rounded_amountPaint,sqArea))
