# Make a function lookup_state that, given a US 
# state abbreviation, returns the state's name.

# We've given you a dictionary with 
# abbreviations as keys and state names as values.
# It's imported for you here:

from US import states

# Example: >>>> lookup_state('NC')
# North Carolina

def lookup_state(abbreviation):
	# Add code here
	return states[abbreviation]



print(lookup_state('NC'))
print(lookup_state('CA'))