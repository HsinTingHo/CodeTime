# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

#a is an array of integers
#d is the number of shifts needed to be made

#Constrain:
# 1 <= d <= n

def rotLeft(a, d):
    num = d%len(a) #if d = the length of the array, the array does not need to be changed
    for shift in range(num):
        p = a.pop(0)
        a.append(p)
    return a

#Evaluate:
#Runtime = O(m)
#Space = O(1)