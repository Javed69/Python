#Make a function switch_case that, given a string, returns the string with uppercasev letters in lowercase and vice-versa. Include punction and other non-cased characters unchanged.
# switch_case('Arg!')
# aRG!
#>>> switch_case('TrInKeT')
# tRiNkEt

def switch_case(string):
	# Add code here
	new_string = ''
	for letter in string:
		if letter.islower():
			new_string += letter.upper()
		else:
			new_string += letter.lower()

	return new_string

print(switch_case('Arg!'))
print(switch_case('TrInKeT!'))

