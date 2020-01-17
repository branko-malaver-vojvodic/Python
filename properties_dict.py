#Reviewing properties of dictionnaries
Month_of_Year={'January': 1, 'February' : 2, 'March': 3, 'April' : 4}
M2={'May': 5, 'June' : 6,}
#Take april out of the dictionary
Month_of_Year.pop('April')
print(Month_of_Year)
#Add M2 to Month_of_Year
Month_of_Year.update(M2)
print(Month_of_Year)
#Print strings in dictionary
Month_of_Year.keys()
print(Month_of_Year.keys())
#Print values in dictionary
Month_of_Year.values()
print(Month_of_Year.values())
