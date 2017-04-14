
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


