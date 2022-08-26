#a="PriYaNsHi"
#b=""
#for i in a:
#    if i.isupper():
#        b+=i.lower()
#    elif i.islower():
#        b+=i.upper()
#    else:
#        b+=i
#print(b)


def swap_string():
	s="PriYaNsHi"
	swapped_string=""
	swapped_string+=s.swapcase()
	
	return swapped_string
swap_string()