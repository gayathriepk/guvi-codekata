#get the numbers
num1=raw_input('Enter the 1st number')
num2=raw_input('Enter the 2nd number')
num3=raw_input('Enter the 3rd number')
#check for thier equality
if num1==num2 and num2==num3 and num3==num1:
  print("numbers are equal")
else:
  if num1>num2 and num1>num3:
    print("!1st number is biggest")
  elif(num2>num3):
    print("Number 2 is biggest")
  else:
    print("Number 3 is biggest")
  