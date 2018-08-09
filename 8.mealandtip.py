mealAmount = float(input("How much is your original bill? \t"))
whatTip = float (input("What percentage would you like to tip? \t"))

tipAmount = mealAmount * (whatTip/100)

print("Your tip amount is: \t", tipAmount)
print("Your total bill amount is: \t", mealAmount+tipAmount)
