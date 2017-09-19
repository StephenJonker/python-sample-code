# uses python3
#
# Written by: Stephen Jonker
# Written on: Tuesday 19 Sept 2017
# Copyright (c) 2017 Stephen Jonker - www.stephenjonker.com
#
# Purpose:
# - basic python program to show sorting a list of number pairs
#
# - Given a list of integer number pairs that will come from STDIN
# - first read in n, the number of lines of input containing input pairs
# - then for 1 to n, read in each integer number pair into a list like structure
#   with each number pair also in a list
# - this will create a list whose elements are lists, that contains integer number pairs
# 	E.g.: [ [1,10], [7,70], [2,20], [4, 40] ]
# - Once read, sort the list based on the first or second list-pair elelment
#
# E.g. input
# 3
# 1 10
# 7 70
# 2 20
# 4 40  
#
# Output: 
# - the sorted list of list pairs
# E.g. [['1', '10'], ['2', '20'], ['4', '40'], ['7', '70']]
# 
# Constraints:
# - the program does not do input validation

if __name__ == "__main__":
	debug = False

	# get the number of lines to input from STDIN
	n = int(input())
	if debug: print("Input n: " + str(n) + " Type: " + str(type(n)) )
	
	numberPair = [] 
	theList = [] 
	
	# Get the lines of input and store in a list of number pairs
	# E.g.: [ [1,10], [7,70], [2,20], [4, 40] ]
	for i in range(0,n):
		numberPair = input().split()	
		theList.append(numberPair)

	if debug: print("The pair list: " + str(theList) + " Type: " + str(type(theList)) )
	if debug: print("Length of the list: " + str(len(theList)))

	# Function to return the first element of the integer list pair
	# Needed to make the "sorted" function work with more complex list elements 
	def sortKey(item):
		return item[0]

	newSortedList = sorted(theList, key=sortKey)

	if debug: print("newSortedList: " + str(newSortedList))

	print(str(newSortedList))

#
# End of file.
# 