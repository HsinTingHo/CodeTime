#Day 10: Binary Numbers
#https://www.hackerrank.com/challenges/30-binary-numbers/problem
   
def consecutive_ones(n):

  count = 0
  while n:
    n &= (n<<1)
    count += 1

  return count

#Evaluate:
#Runtime = O(n)
#Space = O(1)