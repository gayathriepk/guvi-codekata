count=0
prime=int(raw_input("Enter the number"))
for i in range (2,prime):
  if(prime%i==0):
    count+=1
if(count>=1):
  print("not a prime number")
else:
    print("Prime number")