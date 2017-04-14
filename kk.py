#!/usr/bin/python
import sys
import random 

filename = sys.argv[1]
num_file = open(filename, 'r')
#to be used for 
numlist = []
for line in num_file:
	numlist.append(int(line.split()[0]))

#function for generating random instances of problem
def gen_list(numlist=[]):
	for _ in xrange(0,100):
		numlist.append(random.randrange(1000000000000))
	return numlist

#Basic KK Algorithm; takes list and prints the residue
def kar_karp(numlist):
	for i in range(len(numlist)):
		numlist = sorted(numlist)
		big = numlist[len(numlist)-1]
		small = numlist[len(numlist)-2]
		diff = big - small 
		numlist[len(numlist)-1] = diff 
		numlist[len(numlist)-2] = 0
	return numlist[len(numlist)-1]

def kar_karp_test(numlist):
	for i in range(len(numlist)):
		numlist = sorted(numlist)
		big = numlist[len(numlist)-1]
		small = numlist[len(numlist)-2]
		diff = big - small 
		numlist[len(numlist)-1] = diff 
		numlist[len(numlist)-2] = 0
	print numlist[len(numlist)-1]

#Function for running random moves
def rand_move(numlist):
	index_i = random.randrange(len(numlist))
	index_j = random.randrange(len(numlist))
	if(random.random() < .5):
		numlist[index_i] = -numlist[index_i]
	if(random.random() < .5):
		numlist[index_j] = -numlist[index_j]
	return numlist
	print("a=%d,b=%d" % (f(x,n),g(x,n)))
def rand_move_test(numlist):
	"*****Original Numlist"
	index_i = random.randrange(len(numlist))
	print("Index_i: %d, Value: %d" % (index_i, numlist[index_i]))
	index_j = random.randrange(len(numlist))
	print("Index_j: %d, Value: %d" % (index_j, numlist[index_j]))
	if(random.random() < .5):
		numlist[index_i] = -numlist[index_i]
	if(random.random() < .5):
		numlist[index_j] = -numlist[index_j]
	print numlist
#Function for prepartitioning 
def pre_part(numlist, prepart=[], aprime=[]):
	for _ in xrange(len(numlist)):
		prepart.append(random.randrange(0,len(numlist)))
	for i in xrange(0,len(numlist)):
		aprime.append(0)
	for i in xrange(0, len(prepart)):
		aprime[prepart[i]] += numlist[i]
	return aprime

#Function for prepartitioning 
def pre_part_test(numlist, prepart=[], aprime=[]):
	print "Original numlist:"
	print numlist
	for _ in xrange(len(numlist)):
		prepart.append(random.randrange(0,len(numlist)))
	print "Prepartition list:"
	print prepart
	for i in xrange(len(numlist)):
		aprime.append(0)
	for i in xrange(len(numlist)):
		aprime[prepart[i]] += numlist[i]
	print "New aprime"
	print aprime
	return aprime
#invoke methods
def main():
	random.seed(a=None)
	print kar_karp(numlist)

if __name__ == "__main__":
	main()
   
#To execute, might have to run in terminal : chmod +x kk.py 


