#Recurssivity to chop a list into two, the second one will have length splitter
def recSplit(lst,splitter,q=[]):
    s=len(lst)-splitter-1
    if splitter==0 and len(q)==0:
        print(lst)
    elif splitter==0 and len(q)!=0:
        print(lst,q)
        del q[:]
    else:
        q.append(lst[len(lst)-splitter])
        lst.remove(lst[len(lst)-splitter])
        return recSplit(lst,splitter-1,q)
    
