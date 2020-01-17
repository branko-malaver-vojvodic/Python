#Representation of each letter on the entered string in 4 kinds of language
def name_encoding(name):
    print('Char Decimal Hex Binary')
    for i in name:
        code = ord(i)
        print(' {} {:7} {:4x} {:7b}'.format(i, code, code, code))
