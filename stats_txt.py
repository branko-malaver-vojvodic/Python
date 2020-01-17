#Statistics of a txt document
def stats(Document):
    infile = open(Document,'r')
    LineCount = infile.readlines()
    A = len(LineCount)
    print('Line count: '+str(A))
    infile.close()
    infile_1 = open(Document,'r')
    content = infile_1.read()
    WordCount = content.split()
    B = len(WordCount)
    print('Word count: '+str(B))
    CharCount = len(content)
    print('Character count: ' + str(CharCount))
    
