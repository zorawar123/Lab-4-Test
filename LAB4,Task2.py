
import string
 
def small_latters(): 
    dic = dict()
    list1 =[]
    count = 0
    book = 'file.txt' # file.txt stored in book
    with open(book, 'r') as fd:  # open book
        words = fd.read().split() 
        for i in words:
            words1 = i.strip(string.whitespace + string.punctuation)## remove white space ( , ) puctuation
            word = words1.lower() # convert in lower letter
            list1.append(word)
            count += 1
        for j in list1:
            dic[j] =dic.get(j,0) + 1 # declearing variable
            val = dic[j]
            dic.setdefault(j,val) # will set default key 
        print(dic)
        for j in dic:
           if dic[j] ==13: #Check the variable 
               print(j)
        print(count)
small_latters()


