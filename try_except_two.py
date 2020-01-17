#Try-except with specific kinds of errors
def readFile(Document):
    try:
        infile = open(Document,'r')
        contents = infile.read()
        print(contents)
    except IOError:
        print('Input/Output error')
    except ValueError:
        print('Value cannot be read as an integer')
    except:
        print('Other error')
