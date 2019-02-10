import string
 
def small_latters(): 
    dic = []
    book = 'file.txt'
    with open(book, 'r') as fd:
        words = fd.read().split()
        for i in words:
            words1 = i.strip(string.whitespace + string.punctuation)
            word = words1.lower()
            print(word)
small_latters()
