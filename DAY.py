day=raw_input("Enter the day")
day=lower(day)
if(day=="sunday" or day=="saturday"):
	print "yes"
elif(day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday"):
	print "no"
else:
	print "Enter a day"