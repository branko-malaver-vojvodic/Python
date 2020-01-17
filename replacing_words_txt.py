#Replacing the word secret with xxxxxx in a txt
def crypto(Document):
    infile = open(Document,'r')
    contents = infile.read()
    A = contents.replace('secret','xxxxxx')
    print (A)
        
            
    
