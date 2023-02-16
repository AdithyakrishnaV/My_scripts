#hashing is a one way function.So we cannot reverse the hash we can only bruteforce it and check for similar hash
#create hash of password
import hashlib

def hashing(check,word):
    for w in word:
        hasher=hashlib.sha1(w.encode()) 
        c=hasher.hexdigest()
        if(str(c)==check):
            print("\n"+w+"\n")
            break
        else:print("no")

f= open("pass.txt", "r") 
word=f.read().split()
check=input("Enter the hash: \n ")
hashing(check,word)
f.close()

#This code creates a hashlib object for the SHA-1 hash algorithm using the following code:

#The update() method updates the hash object with the bytes in the word. In other words, it adds the bytes of word to the hash object.


#---------------------------------------------------------------------------------------------------------------------------------------------------

# import hashlib

# def hashing(check,word):
    
#     for w in word:
#         hasher=hashlib.sha1(w) 
#         c=hasher.hexdigest()
#         if(str(c)==check):
#             print(w)
#             break
#         else:print("no")
#     # print(c)

# word=[b"hehe",b"fix",b"hello",b"crackme",b"faux"]

# check="23b2dcb1e21e99a2be4faad98ca9dd1a59da99dd"
# hashing(check,word)