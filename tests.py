#Test the rudimentary KK Algorithm
#from kk import kar_karp
import kk
#random.seed(a=None)
example_one = [10,8,7,6,5]
example_two = [4,2,3,2,1]
example_three = [6,2,3,2,1]
'''
print "*******************************\n*******************************"
print "Test 1.0. KK with 10,8,7,6,5\nExpect Residual 2"
kk.kar_karp_test(example_one)
print "Test 1.1. KK with 10,8,7,6,5\nExpect Residual 0"
kk.kar_karp_test(example_two)
print "Test 1.2. KK with 10,8,7,6,5\nExpect Residual 0"
kk.kar_karp_test(example_three)
print "*******************************\n*******************************"
#test the random number generator
rand_prob = kk.gen_list([])
print "Test 2.0. Run numlist generator. Expect 100 random numbers:"
print rand_prob
#Test the prepartition function
print "*******************************\n*******************************"
print "Test 3.0. Testing prepartitioning\n*****************************"
kk.pre_part_test(example_one, [], [])
print "Test 3.1. Testing prepartitioning\n*****************************"
kk.pre_part_test(example_two, [], [])
print "Test 3.2. Testing prepartitioning\n*****************************"
kk.pre_part_test(example_three, [], [])

print "*******************************\n*******************************"
#test the random switch function
print "Test 4.0 Testing Random Move"
print "*******************************\n"
#test the random switch function
kk.rand_move_test(example_one)
print "*******************************\n"
kk.rand_move_test(example_one)
print "*******************************\n"
kk.rand_move_test(example_one)
print "*******************************\n"
kk.rand_move_test(example_one)
print "Test 4.1 Testing Random Move"
print "*******************************\n"
kk.rand_move_test(example_two)
print "*******************************\n"
kk.rand_move_test(example_two)
print "*******************************\n"
kk.rand_move_test(example_two)
print "*******************************\n"
kk.rand_move_test(example_two)
print "*******************************\n"
print "Test 4.2 Testing Random Move"
kk.rand_move_test(example_three)
print "*******************************\n"
kk.rand_move_test(example_three)
print "*******************************\n"
kk.rand_move_test(example_three)
print "*******************************\n"
kk.rand_move_test(example_three)
'''
#Tests for rep_rand_rand
'''
print "*******************************\n"
print "*******************************\n*******************************"
print example_one
print "*******************************\n"
print kk.rep_rand_rand_test(example_one)
print "*******************************\n"

print "*******************************\n"
print "*******************************\n*******************************"
print example_two
print "*******************************\n"
print kk.rep_rand_rand_test(example_two)
print "*******************************\n"

print "*******************************\n"
print "*******************************\n*******************************"
print example_three
print "*******************************\n"
print kk.rep_rand_rand_test(example_three)
print "*******************************\n"
'''
example_one = [10,8,7,6,5]
example_two = [4,2,3,2,1]
example_three = [6,2,3,2,1]
example_four = kk.gen_list(1000000000000, 20, [])
print "*******************************\n"
print "*******************************\n*******************************"
print example_one
print "*******************************\n"
print kk.rep_rand_part_test(example_one)
print "*******************************\n"

print "*******************************\n"
print "*******************************\n*******************************"
print example_two
print "*******************************\n"
print kk.rep_rand_part_test(example_two)
print "*******************************\n"

print "*******************************\n"
print "*******************************\n*******************************"
print example_three
print "*******************************\n"
print kk.rep_rand_part_test(example_three)
print "*******************************\n"

print "*******************************\n"
print "*******************************\n*******************************"
print example_four
print "*******************************\n"
print kk.rep_rand_part_test(example_four)
print "*******************************\n"
