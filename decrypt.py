def main():
    text =  input("Enter the String to  Decrypt : ")

    for i,n in enumerate(text):
        c=ord(n) - i 
        print(chr(c), end="") 
if __name__ == "__main__":
    main()