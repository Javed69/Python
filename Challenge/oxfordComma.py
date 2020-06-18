# Make a function commafy that, given a list of three or more strings
# return a list with commas.
#>>>> commafy(['trinket','learning','fun'])
# trinket, learning, and fun
#>>>> commafy(['lions','tigers','bears'])
# lions, tigers, and bears

def commafy(list):
	# Add code Here
	list[-1] = 'and ' + list[-1]
	return (', '.join(list))
	#return (list)

print(commafy(['trinket','learning','fun']))
print(commafy(['lions','tigers','bears']))  
