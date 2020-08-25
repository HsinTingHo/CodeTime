# Next Prime

# Given a prime number, return the next smallest prime number

# Examples:
# Input: 3
# Output: 5

#Understand

#   Edge cases:
#     Input:
#     Output:

#Match
#brute force

#Plan
#Let set input = n
#loop from n to 2n
#if number is a prime number, return number
#else, continue

def is_prime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True

def Next_Prime(n):
  for i in range(n+1, 2*n):
    if is_prime(i):
      return i
    else:
      continue

#Review
test1 = 3
print(Next_Prime(test1), '| Expected: 5')

#Evaluate
#Runtime = O(n^2)
#Space Compexity = O(1)

#********************************
#  time spend: 10m 10s
#********************************
