#Test the rudimentary KK Algorithm
import sys
print sys.argv[1]
from kk import kar_karp
example_one = [10,8,7,6,5]
example_two = [4,2,3,2,1]
example_three = [6,2,3,2,1]
kar_karp(example_one)
print("\n")
kar_karp(example_two)
print("\n")
kar_karp(example_three)