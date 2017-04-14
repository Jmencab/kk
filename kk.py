
import sys
filename = sys.argv[1]
num_file = open(filename, 'r')
#to be used for 
numlist = []
for line in num_file:
	numlist.append(int(line.split()[0]))
	print line.split()[0]
print numlist 
#Basic KK Algorithm; takes list and prints the residue
def kar_karp(numlist):
	for i in range(len(numlist)):
		numlist = sorted(numlist)
		big = numlist[len(numlist)-1]
		small = numlist[len(numlist)-2]
		diff = big - small 
		numlist[len(numlist)-1] = diff 
		numlist[len(numlist)-2] = 0
	print numlist[len(numlist)-1]


