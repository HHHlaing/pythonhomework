#1. Write a program that generates and prints 50 random integers, each between 3 and 6.


for i in range (50):
    
    from random import randint
    x = randint(3,6)
    print ("Random number between 3 and 6:", x)
       
