from function import *

principal = checkInput_float("Principal?")
intrestRate = checkInput_float("""Rate of intrest?
Ensure the value entered is in the correct format and as a percentage.
ex. a value entered as 7 would be read as 7%""")
years = checkInput("Number of years?")

print("After %s years at %s%%, the investment will be worth $%s." % (years,intrestRate, (1 + (intrestRate/100)) * principal))
