class Difference:
	def __init__(self, a):
		self.__elements = a
		self.maximumDifference = 0


	def computeDifference(self):
		max_element = 101
		min_element = 0
		for element in self.__elements:
			if element < min_element:
				min_element = element
			if element > max_element:
				max_element = element

		self.maximumDifference = max_element - min_element


# e = input()
# a = [int(e) for e in input().split(' ')]
a = [1,2,5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)