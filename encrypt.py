def main():
    text =  input("Enter the String to  encrypt : ")

    for i in text:
        c=ord(i) + text.index(i)
        print(chr(c), end="")
if __name__ == "__main__":
    main()