temperature=int (input ("Enter temperature: "))
user_input = input("From what do you want to convert?: C or F? ")
if user_input== "C":
    print ("Celsius to Fahrenheit is: ",  temperature* 9 / 5 + 32)
elif user_input== "F":
    print ("Fahrenheit to Celsius is: ", temperature* 5 / 9 - 32)
