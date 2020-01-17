#Storing information from a txt Document in a list of lists
def alk_met_super(Document):
    infile = open(Document,'r')
    n_lst = []
    contents = infile.readlines()
    for i in contents:
        lst = i.strip().split('\n')
        n_lst.append(lst)
    print(n_lst)
