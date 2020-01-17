#Function that counts the nonzero elements of a list
def checkNumber(lst):
    res = 0
    for i in lst:
            for item in i:
                a = item > 0
                res = res + a
    return res 
                
                   
               
                
                
