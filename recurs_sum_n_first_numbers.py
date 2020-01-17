#Recurssive sum of n first numbers
def Sum(n):
    if n == 0: 
        return 0
    elif n > 0:
        return Sum(n-1)+n
    else:
        print("Please enter integer values equal or larger than 0")
    