#Recurssive that prints sum of elements on a list
def sum_elements(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_elements(lst[1:])
