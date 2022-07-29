"""
Write a Python program to print all positive numbers in a range.

Your Input and output must look something like this

Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
"""

# list of numbers
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
#list1
for num in list1:
	if num >= 0:
	    print(num, end = " ")

print("\n")
#list2
for num in list2:
	if num >= 0:
	    print(num, end = " ")
