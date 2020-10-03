#New Year Chaos
# Complete the minimumBribes function below.
#Understand:
#Input: [1,2,3,4], [4,3,2,1]
#Output: Too chaotic
#Key objective - how do I find the minimum number of bride?
#   How far away is a number from its original position?

#Plan:
#1. check if a number is at a valid place(within 2 place ahead from original place)
#2. if not, print too chaotic and return
#3. else, count how many bribe each perosn recive by checking in the person's original position, how many number is bigger than the person
def minimumBribes(q):
    bribe = previous = 0

    for i, person in enumerate(q):
        if person - i > 3: #the person bribe more than 2 times
            print('Too chaotic')
            return
        else:
            for j in range(max(person-2,0), i):
                if q[j]>person:
                    bribe += 1

    print(bribe)
    return
    
#Evaluate:
#Runtime: O(n)
#Space: O(1)