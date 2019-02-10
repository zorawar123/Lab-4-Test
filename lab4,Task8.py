import hashlib
import os


def MD5(fname):
    hash_MD5 = hashlib.MD5()
    with open("file.txt", "rb") as f:
        for chunk in iter(lambda: f.read(567), b""):
            hash_MD5.update(chunk)
    return(hash_MD5.hexdigest())

path = os.getenv("/home/student/desktop")
def lookfile(extention):
    for root, subFolder, files in os.walk(path):
        for item in files:
            if item.endswith("."+ str(extention)):
                fileNamePath = str(os.path.join(root,item))
                print(fileNamePath," ",MD5(fileNamePath))


x = raw_input("Enter the location")
lookfile(x)

