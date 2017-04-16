#!/usr/bin/python
import sys
import random 
import timeit
#function for generating random instances of problem
def gen_list(limit, lst_sz, numlist=[]):
	for _ in xrange(lst_sz):
		numlist.append(random.randrange(limit))
	return numlist

#Basic KK Algorithm; takes list and prints the residue; 
#Be aware that this function alters the original list;
#make copy of original list if you'll need it again
def kar_karp(numlist):
	length = len(numlist)
	for i in range(length):
		numlist = sorted(numlist)
		if numlist[length-1] == 0:
			return 0;
		big = numlist[length-1]
		small = numlist[length-2]
		diff = big - small 
		numlist[length-1] = diff 
		numlist[length-2] = 0
	if(numlist[length-1] < 0):
		return - numlist[length-1]
	else:
		return numlist[length-1]

def kar_karp_test(numlist):
	length = len(numlist)
	for i in range(length):
		numlist = sorted(numlist)
		big = numlist[length-1]
		small = numlist[length-2]
		diff = big - small 
		numlist[length-1] = diff 
		numlist[length-2] = 0
	print numlist[length-1]

#Function for running random moves
#Alters original list. 
#Be caureful to make copy if you need original list
#DO you mean > here
def rand_move(numlist):
	length = len(numlist)
	index_i = random.randrange(length)
	index_j = random.randrange(length)
	if(random.random() < .5):
		numlist[index_i] = - numlist[index_i]
	if(random.random() < .5):
		numlist[index_j] = - numlist[index_j]
	return numlist

def rand_move_test(numlist):
	length = len(numlist)
	"*****Original Numlist"
	index_i = random.randrange(length)
	print("Index_i: %d, Value: %d" % (index_i, numlist[index_i]))
	index_j = random.randrange(length)
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
#leaves original list unaltered
def pre_part(numlist, prepart=[], aprime=[]):
	length = len(numlist)
	for _ in xrange(length):
		prepart.append(random.randrange(0,length))
	for _ in xrange(0,length):
		aprime.append(0)
	for i in xrange(0, length):
		aprime[prepart[i]] += numlist[i]
	return aprime

def pre_part_test(numlist, prepart=[], aprime=[]):
	print "Original numlist:"
	length = len(numlist)
	print numlist
	for _ in xrange(length):
		prepart.append(random.randrange(0,length))
	print "Prepartition list:"
	print prepart
	for i in xrange(length):
		aprime.append(0)
	for i in xrange(length):
		aprime[prepart[i]] += numlist[i]
	print "New aprime"
	print aprime
	return aprime
#Doing random resetting with random method
def rep_rand_rand(numlist):
	numlist_best_rand = list(numlist)
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist = rand_move(numlist)
		res = res_calc(numlist)
		if res == 0:
			return res
		if res < best_res:
			numlist_best_rand = list(numlist)
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
			numlist_best_rand = list(numlist)
			best_res = res
	print numlist_best_rand
	return best_res
#Doing random resetting with pp method
def rep_rand_part(numlist):
	numlist_cpy = list(numlist)
	best_res = kar_karp(numlist)
	for _ in xrange(0,25000):
		new_numlist = pre_part(numlist_cpy,[],[])
		res = kar_karp(new_numlist)
		if res == 0:
			return res
		if res < best_res:
			best_res = res
	return best_res
def rep_rand_part_test(numlist):
	numlist_cpy = list(numlist)
	best_res = kar_karp(numlist)
	print best_res
	for _ in xrange(0,25000):
		new_numlist = pre_part(numlist_cpy,[],[])
		res = kar_karp(new_numlist)
		if res == 0:
			print new_numlist
			return res
		if res < best_res:
			best_res = res
			print new_numlist
	return best_res
#function to generate a neighbor
def get_new_neighbor(numlist):
	length = len(numlist)
	index_i = random.randrange(length)
		numlist[index_i] = - numlist[index_i]
	return numlist
#function for hill climbing with repeated random
def hill_climbing_rand(numlist):
	numlist_best_rand = list(numlist)
	best_res = res_calc(numlist_best_rand)
	numlist = rand_move(numlist)
	res = res_calc(numlist)
	for _ in xrange(0,25000):
		if res == 0:
			return res
		if res < best_res:
			numlist_best_rand = list(numlist)
			best_res = res
		numlist = get_new_neighbor(numlist)
		res = res_calc(numlist)
	return best_res
#function for hill climbing with prepartitioning
def hill_climbing_part(numlist): 
	numlist_cpy = list(numlist)
	best_res = kar_karp(numlist)
	for _ in xrange(0,25000):
		new_numlist = pre_part(numlist_cpy,[],[])
		res = kar_karp(new_numlist)
		if res == 0:
			return res
		if res < best_res:
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
	answer_one = kar_karp(numlist)
	print("From textfile, result of KK is: %d" % (answer_one))

	#Repeated Randoms trials
	sum_kk = 0
	sum_rr_rand = 0
	sum_rr_part = 0
	for i in xrange(0,100):
		randlist = gen_list(1000000000000, 100, []);
		randlist_one = list(randlist)
		randlist_two = list(randlist)
		print("****************** TEST %d ******************\n********************************************" % (i))
		start_time = timeit.default_timer()
		kar_res = kar_karp(randlist)
		end_time = timeit.default_timer()
		sum_kk += kar_res
		print("Result from KK: %d" % (kar_res))
		print("Time to run KK: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		rr_rand = rep_rand_rand(randlist_one)
		end_time = timeit.default_timer()
		sum_rr_rand += rr_rand
		print("Result from RR rand: %d" % (rr_rand))
		print("Time to run RR rand: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		rr_part = rep_rand_part(randlist_two)
		end_time = timeit.default_timer()
		sum_rr_part += rr_part
		print("Result from RR part: %d" % (rr_part))
		print("Time to run RR part: %f" % (end_time - start_time))
	
	print("Average residual for KK: %f" % (sum_kk/100))
	print("Average residual for RR rand: %f" % (sum_rr_rand/100))
	print("Average residual for RR part: %f" % (sum_rr_part/100))

if __name__ == "__main__":
	main()
   
#To execute, might have to run in terminal : chmod +x kk.py 


