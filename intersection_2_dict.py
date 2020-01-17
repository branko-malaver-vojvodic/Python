#Function that returns the intersection between two dictionnaries
def dict_intersect(d1,d2):
    d = {}
    for i in d1:
        if i in d2 and d1[i] == d2[i]:
            d[i] = d1[i]
    return d
    
    
        

        

   
