#Counting the number of distinct values in a dictionnary
def count_values(d):
    values = {}
    for key in d:
        values[d[key]] = d[key]
    return len(values)
