# Make a function how_many that, given a list of a number
# and a thing name, returns a grammatically correct sentence
# describing the number of things.

#>>>> how_many[5, 'trinket']
# There are trinkets.
#>>>> how_many[1, 'king']
# There is 1 king.

def how_many(the_list):
	# add code here
	if the_list[0] == 1:
		return 'There is ' + str(the_list[0]) + " " + the_list[-1] + '.'
	else:
		return 'There are ' + str(the_list[0]) + " " + the_list[-1] + 's.'


print(how_many([5, 'trinket']))
print(how_many([1, 'king']))