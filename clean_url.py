# Disallow: /node/add/ Disallow: /search/ Disallow: /user/register Disallow: /user/password Disallow: /user/login Disallow: /user/logout

#enter the items in the url to be removed. Space is the delimeter used
def decode():
  string=input("Enter the encrypted string: \n")
  num=int(input("Enter number of items to remove: "))
  new=string
  i=1
  for i in range(num):
    change=input("Enter the item to remove: ")
    new=new.replace(change,"")
  new=new.split(" ")
  for items in new:
     print(items)
decode()