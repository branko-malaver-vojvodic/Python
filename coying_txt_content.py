#Copying the content of Document1 in Document2
def fcopy(Document1,Document2):
    infile = open(Document1,'r')
    contents = infile.read()
    outfile = open(Document2,'r+')
    outfile.write(contents)
