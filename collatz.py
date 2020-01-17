#Collatz conjecture
print('Please enter a positive number (n > 0), if you do not follow the instruction the programme will not have an end and consequently it will not work properly.')
def collatz(n):
    if n <= 0:
        print('Please enter a positive number, the number below is not a positive number:')
    while n != 1 and n > 0:
        print(n)
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3*n + 1)
    else:
        print (n)
    
    

        
        
