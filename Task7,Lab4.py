file1 = open(file.txt,'r')
file2 = open(file1.txt, 'w')

def sed(word,change,file1,file2):
    try:
        for i in file1:
            if word in i:
                print(i)
                i = i.replace(word,change)
                print(i)
            file2.write(i)
    except:
        print("Not Possible to replace")
    finally:
        print("This will execute")


sad("bob","Momi",file1,file2)