# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.
# The slots are sorted by slots’ start time.

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12

def overlap(a, b):
  if a[1] < b[0] or b[1] < a[0]:
    return False
  else:
    return True
  
def meeting_planner(slotsA, slotsB, dur):
  B_current = 0
  B_length = len(slotsB)
  for A in slotsA:
    if A[1] - A[0] >= dur:
      for i in range(B_current, B_length):
        B = slotsB[i]
        
        if B[0]>A[1]:
          break
        if overlap(A, B) and B[1]-B[0] >= dur:
          A.extend(B)
          A.sort()
          if A[2]-A[1] >= dur:
            return [A[1], A[1]+dur]
        B_current = i
  return []

#Evaluate
#Runtime: O(n+m)
#Space: O(1)