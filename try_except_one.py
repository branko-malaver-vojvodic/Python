#try-except exercise
try:
    while True:
        x = input('Enter your area-code: ')
        y = int(x)
        print('Your code-area is {}'.format(y))
        break
except:
    print('Only numbers accepted 0-9')
    

