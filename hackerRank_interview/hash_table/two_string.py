#Two Strings
#https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def twoStrings(s1, s2):
    set_1 = set(s1)
    if set_1.difference(set(s2)) == set_1:
        return 'NO'
    else:
        return 'YES'

#Evaluate
#Runtime = O(n)
#Space = O(n)