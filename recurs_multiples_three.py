#Recurssive function for multiples of three
def f(n):
    'Please enter a positive number. n > 0.'
    if n > 0:
        if n == 1:
            return 3
        else:
            return f(n-1) + 3
    else:
        print('Please introduce a positive number')
