#Recurssive version of pairs1
def pairs2(lst,s):
    q=[]
    lst.sort(key=int)
    k=len(lst)-1
    if k==0:
        print('False')
    elif lst[0]+lst[1]>s or lst[k-1]+lst[k]<s:
        print('False')
    elif lst[0]+lst[1]<=s:
        for i in range(1,k+1):
            if lst[0]+lst[i]==s:
                q.append(1)
        if 1 in q:
            print('True')
        else:
            lst.remove(lst[0])
            return pairs2(lst,s)
                
        
    
                
                
