#Checking if it is a geometric sequence
def geometric(lst):
    common_ratio = lst[1]/float(lst[0])
    for i in range(1, len(lst)):
        if lst[i]/float(lst[i-1]) != common_ratio:
            return False
    return True
            
        
        
        
        
