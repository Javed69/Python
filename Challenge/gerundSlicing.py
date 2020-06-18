# Make a function gerund_infinitive that, given a string ends with 'ing'
# returns the rest of the string prefixed with 'to'.
# If it does not end with 'ing', return 'That's not a gerund!'

#>>>> gerund_infinitive('building')
# to build
#>>>> gerund_infinitive('build')
# That's not a gerund!

def gerund_infinitive(string):
	# Add code here
	if string[-3:] == 'ing':
		return 'to ' + string[:-3]
	else:
		return "That's not a gerund!"



print(gerund_infinitive('building'))
print(gerund_infinitive('build'))