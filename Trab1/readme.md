how to use "filename".in to execute problem:

./problem < inputs/"filename".in > outputs/entrada*/"outputfile".out

in which "outputfile" can be named in command line. * is the number of input.

inputGenerator.py can be used to create new input examples.
saveLog.py is used to create files with 5 runtime samples for any test.
solution.cpp is the parallelized version of problem.cpp

ref (read later): https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

input files:

entrada1: n = 60000, k = 40 (taken from source code)
entrada2: n = 40000, k = 20
entrada3: n = 90000, k = 80
entrada4: n = 100000, k = 90
entrada7: n = 150000, k = 120

entrada2 > entrada1 > entrada3 > entrada4

input file suggestions:
entrada5: same as entrada1 but k=20
entrada6: same as entrada1 but k=60

entrada5 > entrada1 > entrada6 >

teste0.txt shows runtime logs and average runtime before using openMP.
