#Array Manipulation
#https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        #record the relationship between numbers
        a, b = query[0]-1, query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
    max_num = 0
    current = 0
    for elem in array:
        current += elem
        if current > max_num:
            max_num = current
    return max_num

    #Evaluate
    #Runtime = O(n+m)
    #Space = O(n)