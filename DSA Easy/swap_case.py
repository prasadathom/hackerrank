#my solution for Swap Case 
def swap_case(s):
    swap = s.swapcase()
    return swap
    

#another solution without using .swapcase()
def swap_case(string):
    newstring = ''
    count1 = 0
    count2 = 0
    count3 = 0

    for a in string:
    	if (a.isupper()) == True:
		    count1 += 1
		    newstring += (a.lower())

    	elif (a.islower()) == True:
		    count2 += 1
		    newstring += (a.upper())

	    elif (a.isspace()) == True:
		    count3 += 1
		    newstring += a
  
  return newstring
