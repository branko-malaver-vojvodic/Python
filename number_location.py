#Function that tells you where the number is located
def checkRange(x):
    if x < 25:
        return('The number is below 25')
    elif x >= 26 and x <= 50:
        return('The number is between 26 and 50')
    elif x >= 50:
        return('The number is over 50')
    else:
        return('The number is 25')
