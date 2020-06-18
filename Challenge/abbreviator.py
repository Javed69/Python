# Make a function abbreviator that, given a string, return the string
# if the string is 5 characters. Otherwise, return 
# four characters of the string, followed by a ".".

#>>>> abbreviator('Trinket')
# Trin.
#>>>> abbreviator('argh!')
# argh!

def abbreviator(string):
	# Add code Here
	if len(string) < 5:
		return string + '!'
	else:
	    return string[0:4] + '.'


print(abbreviator('Trinket'))
print(abbreviator('arg'))
