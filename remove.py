def decode():
  string=input("Enter the  string: \n")
  num=int(input("Enter number of items to remove: "))
  new=string
  i=1
  for i in range(num):
    change=input("Enter the item to remove: ")
    new=new.replace(change,"")
  print(new)
decode()