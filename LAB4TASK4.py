import string
def different_word(word1):
    myfile = open("file.txt","r")
    wordsl = open(word1,"r")
    p = string.punctuation
    histo = dict()
    counter = 0
    word1 = []
    newlist = []
    newwords = []
    for my in myfile:
        my = my.strip()
        for c in p:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            word1.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    for word in wordsl:
        word = word.strip()
        word = word.lower()
        newwords.append(word) 
    for key, value in histo.items():
        if key not in newwords:
            print(key)

x = input("Enter file name of list of words:")
different_word(x)


