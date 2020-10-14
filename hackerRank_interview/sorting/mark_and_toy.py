#Mark and toy
#https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def maximumToys(prices, k):
    prices.sort()
    price_sum = 0
    count = 0
    for p in prices:
        if price_sum + p <= k:
            price_sum += p
            count += 1
        else:
            break
    return count

#Evaluate
#Runtime: O(n)
#Space: O(1)