#!/bin/python3

import sys

#n = int(input().strip())
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr = 	[1,2,3,4]
reverse_array = []
for i in range(len(arr)):
	reverse_array.append(arr[len(arr)-i-1])

# output_string = ''
# for i in range(len(reverse_array)):
# 	output_string += str(reverse_array[i]) + ' '

# print(output_string)

print(' '.join(str(i) for i in reverse_array))