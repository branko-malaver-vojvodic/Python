#Function that tells the strength of an acid
def ph_level(x):
    if x>=0 and x<=4:
        print('It is a strong acid.')
    if x>=5 and x<=6:
        print('It is a weak acid.')
    if x==7:
        print('It is neutral')
    if x>=8 and x<=9:
        print('It is a weak base')
    if x>=10 and x<=14:
        print('It is a strong base')
    else: 
        print("Enter a number between 0 and 14")
    

                        

        
