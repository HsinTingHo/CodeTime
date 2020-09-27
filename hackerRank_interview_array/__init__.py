# Given a 6x6  2D Array:
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

def hourglassSum(arr):
    max_sum = 0
    i = 0
    j = 0
    
    for i in range(0, 4):
        for j in range(0, 4): 
            hour = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if hour > max_sum:
                max_sum = hour
    
    return max_sum

#Evaluate:
#Runtime: O(n^2)
#Space: O(1) 