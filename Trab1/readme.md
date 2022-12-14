how to use "filename".in to execute problem:

./problem < "filename".in > "outputfile".out

in which "outputfile" can be named in command line.

inputGenerator.py can be used to create new input examples.
solution.cpp is the parallelized version of problem.cpp

ref (read later): https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

input files:

entrada1: n = 60000, k = 40 (taken from source code)
entrada2: n = 40000, k = 20
entrada3: n = 90000, k = 80
entrada4: n = 100000, k = 90

entrada2 > entrada1 > entrada3 > entrada4

teste0.out shows runtime before parallelization.
