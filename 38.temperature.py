temperature=int (input ("Enter temperature: "))
if temperature < -273.15:
    print ("The temperature is invalid because it is below absolute zero.")
if temperature == -273.15:
    print ("The temperature is absolute zero.")
if -273.15 < temperature < 0:
    print ("The temperature is below freezing.")
if temperature == 0:
    print ("The temperature is at the freezing point.")
if temperature == 100:
    print ("The temperature is at the boiling point.")
if 0 < temperature < 100:
    print ("The temperature is in the normal range.")
if temperature > 100:
    print ("The temperature is above the boiling point.")    
    

    

