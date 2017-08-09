#get the numbers
num1=int(raw_input('Enter the 1st number'))
num2=int(raw_input('Enter the 2nd number'))
num3=int(raw_input('Enter the 3rd number'))
if num1==num2 and num2==num3 and num3==num1:
  print("numbers are equal")
else:
  num=[num1,num2,num3]
  print (max(num))
