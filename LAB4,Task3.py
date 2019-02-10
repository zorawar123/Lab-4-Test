import string
def small(): 
    dic = dict()
    list1 =[]
    count = 0
    book = 'file.txt'
    with open(book, 'r') as fd:  # same code as 1st program, will lower case  words by striping the words
        words = fd.read().split()
        for i in words:
            words1 = i.strip(string.whitespace + string.punctuation)
            word = words1.lower()
            count += 1
            list1.append(word)
        dict_list(list1,dic) 
def dict_list(list1,dic):
    for j in list1:
        dic[j] =dic.get(j,0) + 1
        value1 = dic[j]
        dic.setdefault(j,value1)
    print(dic)
    repeted_word(dic)    
def repeted_word(dic):
    list2 = []
    sub = []
    i = dic.items()
    for key,value in i:
        list2.append(key)
        list2.append(value)
    for i in range(0,len(list2),2):
        sub.append(list2[i:i+2])
    sub.sort(key = lambda x:x[1],reverse = True) # lambda is a special function will return the key value as x and reverse is used to traverse the list 
    for i in range(0,20):
        list3 = sub[i]
        for  j in range(0,len(list3),2):
            print(list3[j])
small()
