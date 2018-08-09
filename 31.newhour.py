x=int(input ("Enter hour: "))
y=int(input ("How many hours ahead? "))
z=x+y;
if (z>12):
    print ("New hour: ",(z-12), "o'clock")
else:
    print ("New hour: ", z, "o'clock")
