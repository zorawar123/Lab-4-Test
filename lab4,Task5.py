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
    sub.sort(key = lambda x:x[1],reverse = True)
    number = 0
    a = []
    b = []
    print("Hell" ,'Lov',"Father" sep = '\t\t\t')
    for i in range(len(sub)):
        sub1 = sub[i]
        number += 1
        log1 = math.log10(number)
        a.append(log1)
        for j in range(0,len(sub1)-1):
            log2 = math.log10(sub1[j+1])
            a.append(log2)
            print(number, sub1[j], sub1[j + 1],log1,log2)
   matplot(a,b)
import matplotlib.pyplot as pyplot
def matplot(log1,log2):
    pyplot.clf()
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.title(“zipf")
    pyplot.xlabel(“rank”)
    pyplot.ylabel(“frequency”)
    pyplot.plot(log1,log2)
    pyplot.show()
matplot(log1,log2)