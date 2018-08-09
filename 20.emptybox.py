n=int(input('Please enter a positive integer between 1 and 15: '))
for col in range(n):
    for row in range(n):
        print('*' if col in(0,(2*n)+1) or row in(0,n+1) else ' ', end=' ')
    print()
