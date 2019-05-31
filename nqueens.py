"""
CISC 352    |   Assignment 1
Isaac Hogan	|	10188271
Zane Little |   10179568
"""
import random
import math
import time


"""
Generates an incomplete solution for n queens using a greedy algorithm
"""
def generateGreed(n):
	pos = [-1] * n
	vrt = [0] * n
	rtl = [0] * ((2*n) - 1)
	ltr = [0] * ((2*n) - 1)
	flagged = []
	cols = set()
	for i in range(n): 
		cols.add(i)

	if n == 6:
		temp = cols.pop()
		cols.add(temp)
	for row in range(n):
		left = len(cols)
		for i in range(left):
			col = cols.pop()
			if(rtl[row + col] == 0) and (ltr[row + ((n-1) - col)] == 0):
				pos[row] = col
				vrt[col] = 1
				rtl[row + col] = 1
				ltr[row + ((n-1) - col)] = 1
				break
			else:
				cols.add(col)
		if pos[row] == -1:
			flagged.append(row)

	for row in flagged:
		col = cols.pop()
		pos[row] = col
		vrt[col] = 1
		rtl[row + col] += 1
		ltr[row + ((n-1) - col)] += 1
		
	return [pos, vrt, rtl, ltr]


"""	
Fixes a partial solution with the min conflicts algorithm
"""		
def minConflicts(list):
	ltr = list.pop()
	rtl = list.pop()
	vrt = list.pop()
	pos = list.pop()
	n = len(pos)
	conf = conflicting([pos,vrt,rtl,ltr])

	counter = 0
	fail = False
	
	while conf != []:
		random.shuffle(conf)
		row = conf.pop()
		conflicts = []
		lowConflicts = []
		lowest = math.inf
		
		for col in range(n):
			conflicts.append(0)
			conflicts[col] += vrt[col]
			conflicts[col] += rtl[row + col]
			conflicts[col] += ltr[row + ((n-1) - col)]
			if col == pos[row]:
				conflicts[col] = math.inf
			if conflicts[col] < lowest:
				lowConflicts = []
				lowest = conflicts[col]
			if conflicts[col] == lowest:
				lowConflicts.append(col)
		
		random.shuffle(lowConflicts)
		swap = lowConflicts.pop()
		col = pos[row]
		
		vrt[col] -= 1
		rtl[row + col] -= 1
		ltr[row + ((n-1) - col)] -= 1
		
		vrt[swap] += 1
		rtl[row + swap] += 1
		ltr[row + ((n-1) - swap)] += 1
		
		pos[row] = swap
		if counter < 10000:
			conf = conflicting([pos,vrt,rtl,ltr])
		else:
			fail = True
			break
		counter += 1
	
	#print("Number of swaps: " + str(counter)) #left in for evaluation purposes
	
	if fail:
		return []
	else:
		return pos


"""
Returns a list with all elements currently experiencing conflicts
"""
def conflicting(list):
	ltr = list.pop()
	rtl = list.pop()
	vrt = list.pop()
	pos = list.pop()
	n = len(pos)
	conflicts = []
	
	for col in range(n):
		row = pos[col]
		if (vrt[row] > 1) or (rtl[row + col] > 1) or (ltr[col + ((n-1) - row)] > 1):
			conflicts.append(col) #col
	return conflicts

"""
Takes a list indicating the solution in base 1 and prints this to the file 'nqueens_out.txt'
"""
def writeToFile(solution):
    # This is used to convert solution to base 1 as it is currently base 0
    base_1_sol = [x+1 for x in solution] 
    file = open('nqueens_out.txt', 'a+')
    file.write("[" + ','.join(map(str, base_1_sol)) + "]\n")
    file.close

	
"""
This function reads a specified file and calls the nqueens function
with each line sepecifying the size of the grid.
"""
def readInput(fileName):
	file = open(fileName, 'r')
	line = file.readline()
	attempt = 1
	start = time.time() # performance metric
	while line:
		gridSize = int(line)
		solution = minConflicts(generateGreed(gridSize))
		if (solution == []) and (attempt <= 10):
			print(str(gridSize) + ": Fail. Retrying...", sep='')
			attempt += 1
		else:
			if (attempt <= 10):
				print(str(gridSize) + ": Success.", sep='')
			else:
				print(str(gridSize) + ": Fail limit exceeded. Writing dummy list.", sep='')
				solution = [0]*gridSize
			writeToFile(solution)
			print("Completed in", time.time() - start, "seconds.")
			line = file.readline()
			attempt = 1
			start = time.time() # performance metric
	file.close

	
"""
Run instruction
"""
readInput("nqueens.txt")	