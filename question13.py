from function import *

principal = checkInput_float("Principal?")
intrestRate = checkInput_float("""Rate of intrest?
Ensure the value entered is in the correct format and as a percentage.
ex. a value entered as 7 would be read as 7%""")
years = checkInput("Number of years?")
timesCompounded = checkInput("Intrest compounded?")

total = principal* (1 + (intrestRate/timesCompounded)) ** (timesCompounded * years)
print("After %s years at %s%% compounded % times, the investment will be worth $%s." % (years,intrestRate,timesCompounded,round(total,2)))
