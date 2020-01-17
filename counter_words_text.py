#Counter of how many times a word is repeated on a string text
def count_Duplicate(x):
    WordSplit = x.split()

    counters = {}
    for word in WordSplit:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    for word in counters:
        if counters[word] == 1:
            print('{:12} appears {} time.' .format(word, counters[word]))
        else:
            print('{:12} appears {} times.' .format(word, counters[word]))
