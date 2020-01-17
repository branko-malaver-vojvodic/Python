#Returns True if 2 elements in lst summed are equal to s
def pairs1(lst,s):
    q=[]
    r=len(lst)
    for i in range(0,r):
        for j in range(0,r):
            if lst[i]+lst[j]==s and i!=j:
                q.append(1)
    if len(q)==0:
        print('False')
    else:
        print('True')


        
    
                
                
