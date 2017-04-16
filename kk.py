#!/usr/bin/python
import sys
import random 
import timeit
import math
#function for generating random instances of problem
def gen_list(limit, lst_sz, numlist=[]):
	for _ in xrange(lst_sz):
		numlist.append(random.randrange(limit))
	return numlist
#Doing random resetting with random method
def rand_solution(numlist, len):
	for i in xrange(len):
		if random.random() < .5:
			numlist[i] = -numlist[i]
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
def rand_move(numlist):
	length = len(numlist)
	index_i = random.randrange(length)
	index_j = random.randrange(length)
	if(random.random() < .5):
		numlist[index_i] = - numlist[index_i]
	if(random.random() < .5):
		numlist[index_j] = - numlist[index_j]
	return numlist
#Testing previous function
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
#Function to create a prepartitioning solution list P  
def new_pre_partP(length, prepart=[]):
	for _ in xrange(length):
		prepart.append(random.randrange(0,length))
	return prepart
#Function for prepartitioning
#leaves original list unaltered
def pre_part(numlist, prepart, aprime=[]):
	length = len(numlist)
	for _ in xrange(0,length):
		aprime.append(0)
	for i in xrange(0, length):
		aprime[prepart[i]] += numlist[i]
	return aprime
#function to test prepartitioning 
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
#function for repeated random algorithm random solution
def rep_rand_rand(numlist):
	numlist = rand_solution(numlist, 100)
	numlist_best_rand = list(numlist)
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist = rand_solution(numlist, 100)
		res = res_calc(numlist)
		if res == 0:
			return res
		if res < best_res:
			numlist_best_rand = list(numlist)
			best_res = res
	return best_res
#function to test repeated rand algorithm
def rep_rand_rand_test(numlist):
	numlist = rand_solution(numlist, 100)
	numlist_best_rand = numlist
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist = rand_solution(numlist, 100)
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
	length = len(numlist)
	pre_part_P = new_pre_partP(length,[])
	new_numlist = pre_part(numlist, pre_part_P,[])
	best_res = kar_karp(new_numlist)
	for _ in xrange(0,25000):
		pre_part_P = new_pre_partP(length, [])
		new_numlist = pre_part(numlist,pre_part_P,[])
		res = kar_karp(new_numlist)
		if res == 0:
			return res
		if res < best_res:
			best_res = res
	return best_res
def rep_rand_part_test(numlist):
	length = len(numlist)
	numlist_cpy = list(numlist)
	best_res = kar_karp(numlist)
	print best_res
	for _ in xrange(0,25000):
		new_pre_partP = pre_part_P(length,[])
		new_numlist = pre_part(numlist_cpy, new_pre_partP,[])
		res = kar_karp(new_numlist)
		if res == 0:
			return res
		if res < best_res:
			best_res = res
	return best_res
#function for hill climbing with repeated random
def hill_climbing_rand(numlist):
	length = len(numlist)
	numlist_rand_sol = rand_solution(numlist,length)
	numlist_best_rand = numlist_rand_sol
	best_res = res_calc(numlist_best_rand)
	for _ in xrange(0,25000):
		numlist_rand_sol = rand_move(numlist_rand_sol)
		res = res_calc(numlist_rand_sol)
		if res == 0:
			return res
		if res < best_res:
			numlist_best_rand = list(numlist_rand_sol)
			best_res = res
	return best_res
#function to generate a neighbor for the prepartitioning
def rand_move_part(prepart):
	length = len (prepart)
	index_i = random.randrange(length)
	index_j = random.randrange(length)
	prepart[index_i] = index_j
	return prepart
#function for hill climbing with prepartitioning
def hill_climbing_part(numlist):
	length = len(numlist) 
	pre_part_P = new_pre_partP(length, [])
	numlist_cpy = pre_part(numlist, pre_part_P, [])
	best_res = kar_karp(list(numlist_cpy))
	for _ in xrange(0,25000):
		pre_part_P = rand_move_part(pre_part_P)
		new_numlist = pre_part(numlist_cpy,pre_part_P,[])
		res = kar_karp(list(new_numlist))
		if res == 0:
			return res
		if res < best_res:
			best_res = res
	return best_res
#Function for the annealing probability
def T(iter):
	return (math.pow(10,10))*math.pow(0.8,(iter/300))
#function for simulated annealing random
def sim_annealing_rand(numlist):
	length = len(numlist)
	numlist_sol = rand_solution(numlist, length)
	res_sol = res_calc(numlist_sol)
	numlist_sol2 = list(numlist_sol)
	res_sol2 =  res_sol
	for i in xrange(0,25000):
		numlist_sol1 = rand_move(list(numlist_sol))
		res_sol1 = res_calc(numlist_sol1)
		if res_sol1 < res_sol:
			numlist_sol = list(numlist_sol1)
			res_sol = res_calc(numlist_sol)
		else :
			rand_prob = random.random()
			if rand_prob <=  math.exp(-(res_sol1-res_sol)/T(i)):
				numlist_sol = list(numlist)
		if res_calc(numlist_sol)< res_calc(numlist_sol2):
			numlist_sol2 = list(numlist_sol) 
	return res_sol2
#function for simulated annealing: prepartitioning
def sim_annealing_part(numlist):
	length = len (numlist)
	pre_part_P = new_pre_partP(length, [])
	numlist_sol = pre_part(numlist, pre_part_P, [])
	res_sol = kar_karp(list(numlist_sol))
	numlist_sol2 = list(numlist_sol)
	res_sol2 = res_sol
	for i in xrange(0,25000):
		pre_part_P = rand_move_part(pre_part_P)
		numlist_sol1 = pre_part(numlist, pre_part_P,[])
		res_sol1 = kar_karp(list(numlist_sol1))
		if res_sol1< res_sol:
			numlist_sol = list(numlist_sol1)
			res_sol = kar_karp(list(numlist_sol))
		else: 
			rand_prob = random.random()
			if rand_prob <=  math.exp(-(res_sol1-res_sol)/T(i)):
				numlist_sol = list(numlist)
		if kar_karp(list(numlist_sol))< kar_karp(list(numlist_sol2)):
			numlist_sol2 = list(numlist_sol) 
			res_sol2 = kar_karp(list(numlist_sol2))
	return res_sol2
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
	sum_hc_rand = 0
	sum_hc_part = 0
	sum_sa_rand = 0
	sum_sa_part = 0
	for i in xrange(0,10):
		randlist = gen_list(1000000000000, 100, []);
		print("****************** TEST %d ******************\n********************************************" % (i))
		start_time = timeit.default_timer()
		kar_res = kar_karp(list(randlist))
		end_time = timeit.default_timer()
		sum_kk += kar_res
		print("Result from KK: %d" % (kar_res))
		print("Time to run KK: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		rr_rand = rep_rand_rand(list(randlist))
		end_time = timeit.default_timer()
		sum_rr_rand += rr_rand
		print("Result from RR rand: %d" % (rr_rand))
		print("Time to run RR rand: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		rr_part = rep_rand_part(list(randlist))
		end_time = timeit.default_timer()
		sum_rr_part += rr_part
		print("Result from RR part: %d" % (rr_part))
		print("Time to run RR part: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		hc_rand = hill_climbing_rand(list(randlist))
		end_time = timeit.default_timer()
		sum_hc_rand += hc_rand
		print("Result from HC rand: %d" % (hc_rand))
		print("Time to run HC rand: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		hc_part = hill_climbing_part(list(randlist))
		end_time = timeit.default_timer()
		sum_hc_part += hc_part
		print("Result from HC part: %d" % (hc_part))
		print("Time to run HC part: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		sa_rand = sim_annealing_rand(list(randlist))
		end_time = timeit.default_timer()
		sum_sa_rand += sa_rand
		print("Result from SA rand: %d" % (sa_rand))
		print("Time to run SA rand: %f" % (end_time - start_time))
		start_time = timeit.default_timer()
		sa_part = sim_annealing_part(list(randlist))
		end_time = timeit.default_timer()
		sum_sa_part += sa_part
		print("Result from SA part: %d" % (sa_part))
		print("Time to run SA part: %f" % (end_time - start_time))
	
	print("Average residual for KK: %f" % (sum_kk/100))
	print("Average residual for RR rand: %f" % (sum_rr_rand/100))
	print("Average residual for RR part: %f" % (sum_rr_part/100))
	print("Average residual for HC rand: %f" % (sum_hc_rand/100))
	print("Average residual for HC part: %f" % (sum_hc_part/100))
	print("Average residual for SA rand: %f" % (sum_sa_rand/100))
	print("Average residual for SA part: %f" % (sum_sa_part/100))



if __name__ == "__main__":
	main()
   
#To execute, might have to run in terminal : chmod +x kk.py 


