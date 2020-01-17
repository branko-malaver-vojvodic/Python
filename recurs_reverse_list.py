#Recurssive to inverse the list order
def recReverse(lst):
    if lst == []:
        return lst
    else:
        A = lst [0]
        B = lst[1:]
        return recReverse(B) + [A]
