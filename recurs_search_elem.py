#Recurssive to search an element in a sorted list of numbers
def searchList(lst,n,q=0):
    try:
        if n==lst[q]:
            print ('true')
        elif n!=lst[q]:
            searchList(lst,n,q+1)
    except:
        print('false')


