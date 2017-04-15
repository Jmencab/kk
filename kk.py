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
	if(numlist[len(numlist)-1] < 0):
		return - numlist[len(numlist)-1]
	else:
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
		numlist[index_i] = - numlist[index_i]
	if(random.random() < .5):
		numlist[index_j] = - numlist[index_j]
	return numlist

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

#Function for determining residual from random method
def res_calc(numlist):
	res = 0
	for i in xrange(len(numlist)):
		res += numlist[i]
	if(res < 0):
		return -res
	else:
		return res

#Function for prepartitioning 
def pre_part(numlist, prepart=[], aprime=[]):
	for _ in xrange(len(numlist)):
		prepart.append(random.randrange(0,len(numlist)))
	for _ in xrange(0,len(numlist)):
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
#Doing random resetting with random method
def rep_rand_rand(numlist):
	numlist_best_rand = numlist
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist = rand_move(numlist)
		res = res_calc(numlist)
		if res == 0:
			return res
		if res < best_res:
			numlist_best_rand = numlist
			best_res = res
	return best_res
def rep_rand_rand_test(numlist):
	numlist_best_rand = numlist
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist = rand_move(numlist)
		res = res_calc(numlist)
		if res == 0:
			print numlist
			return res
		if res < best_res:
			numlist_best_rand = numlist
			best_res = res
	print numlist_best_rand
	return best_res
#Doing random resetting with pp method
def rep_rand_part(numlist):
	numlist_best_part = numlist 
	best_res = kar_karp(numlist)
	#original numlist gone after kar_karp
	for _ in xrange(0,25000):
		numlist = pre_part(numlist_best_part,[],[])
		#prepart leaves numlist in tact
		list_temp = numlist
		res = kar_karp(numlist)
		#kar_karp obliterates numlist
		if res == 0:
			return res
		if res < best_res:
			numlist_best_part = list_temp
			best_res = res
	return best_res

#invoke methods
def main():
	random.seed(a=None)
	#First part of output
	filename = sys.argv[1]
	num_file = open(filename, 'r')
	numlist = []
	for line in num_file:
		numlist.append(int(line.split()[0]))
	print kar_karp(numlist)

	#Repeated Randoms trials
	sum_kk = 0
	sum_rr_rand = 0
	sum_rr_part = 0
	for _ in xrange(0,100):
		randlist = gen_list([]);
		randlist_one = randlist
		randlist_two = randlist
		print "*******************\n*******************"
		kar_res = kar_karp(randlist)
		sum_kk += kar_res
		print("Result from KK: %d" % (kar_res))

		rr_rand = rep_rand_rand(randlist_one)
		sum_rr_rand += rr_rand
		print("Result from RR rand: %d" % (rr_rand))

		rr_part = rep_rand_part(randlist_two)
		sum_rr_part += rr_part
		print("Result from RR part: %d" % (rr_part))
	
	print("Average residual for KK: %lu" % (sum_kk/100))
	print("Average residual for RR rand: %lu" % (sum_rr_rand/100))
	print("Average residual for RR part: %lu" % (sum_rr_part/100))

if __name__ == "__main__":
	main()
   
#To execute, might have to run in terminal : chmod +x kk.py 


