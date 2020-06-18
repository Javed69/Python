# String in morse code. CODE.py contains a dictionary 
# mapping capital letters to morse code, which we've already

#>>>> morify('TRINKET')
# -.-...-.-.-.-
#>>>> morify('Z')
# --..

# This imports a dictionary called CODE that maps letters to morse code
from CODE import MORSE_CODE_DICT

def morify(string):
	# Add code here
	final_string = ""
	for letter in string:
		final_string += MORSE_CODE_DICT[letter]
	return final_string



print(morify('TRINKET'))