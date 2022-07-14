# compare 2 different methods 
import timeit

def sum1(b):
  final_sum = 0
  for x in range(b+1):
    final_sum += x 
  return final_sum 

def sum2(b):
  return(b*(b+1))/2

# give timeit module access to the above 2 functions, pass setup parameter. 
# compare two functions' performance
# source: https://docs.python.org/3.9/library/timeit.html
if __name__ =='__main__':
  print(timeit.timeit("sum1(100)", setup="from __main__ import sum1"))
  print(timeit.timeit("sum2(100)", setup="from __main__ import sum2"))

# output
# 3.5961944
# 0.11140060000000007