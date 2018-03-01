number=int(input("Enter number: "))
copy=number
rev=0
while(copy>0):
    dig=copy%10
    rev=rev*10+dig
    copy=copy/10
if(number==rev):
	print "yes"
else:
	print "no"