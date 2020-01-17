#Recurssivity to have a list with all the original elements duplicated
def recDup(lst):
    if lst == []:
        return lst
    else:
        A = lst[0:1]
        B = lst[1:]
        return (A*2) + recDup(B)
