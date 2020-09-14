# 218. The Skyline Problem(https://leetcode.com/problems/the-skyline-problem/description/)
# The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

# The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

# For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

# Notes:

# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

#Plan:
#1. initiate contours array
#2. loop through building array until unoverlap 
#3.   within this elements, sort with height
#4.        higher range = heighest (Li, Ri)
#5.        if the left < higher range Li, higer range Li = Li, put (Li,h)in countor
#6.        else if the right > higer range Ri, higher range Ri = Ri

def overlap(b1, b2):
  left = min(b1, b2)
  right = max(b1, b2)
  if left[1]<right[0]:
    return False
  else:
    return True

def getSkyline(buildings):
  contours = []
  num_of_building = len(buildings)
  group_start = group_end = 0
  for i in range(1, num_of_building):
    if not overlap(buildings[i-1], buildings[i]) or i == num_of_building-1:
      group_end = i
      print('start: %d | end: %d'%(group_start, group_end))
      group = buildings[group_start: group_end]
      print('Group', group)
      if group_end < num_of_building-1:
        group_start = i+1
    
      group.sort(key=lambda x:x[2]) #sort building by height
      higher_range = [group[0][0], group[0][1]]
      contours.append([group[0][0], group[0][2]])
      
      for building in group:
        if building[0]<higher_range[0]:
          higher_range[0] = building[0]     
        if building[1]>higher_range[1]:
          higher_range[1] = building[1]
        if not overlap(higher_range, building[0:2]):
          contours.append([building[0], building[2]])
      contours.append([building[1],0])
  return contours
      




#test
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

print(getSkyline(buildings))
print('Expected:')
print([[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
#32m