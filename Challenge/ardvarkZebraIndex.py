# make a function aardvark that, given a string, returns 'aardvark'
# if the string starts with an a. Otherwise, return 'zebra'.
#>>>> aardvark('arg')
# aardvark
#>>>> aardvark('Trinket')
# zebra

def aardvark(string):
	# Add code here
	if string[0] == 'a':
		return 'aardvark'
	else:
		return 'zebra'


print(aardvark('arg'))
print(aardvark('Trinket'))
