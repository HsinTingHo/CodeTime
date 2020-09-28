#Minimum Swaps 2


def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            to_swap = arr[i]-1
            arr[i], arr[to_swap] = arr[to_swap], arr[i]
            count += 1
    return count

#Evaluate:
#Runtime = O(n^2)
#Space = O(1)