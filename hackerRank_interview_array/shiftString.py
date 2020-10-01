def getShiftedString(s, leftShifts, rightShifts):
    i = (leftShifts - rightShifts) % len(s)
    return s[i:]+s[:i]

#Evaluate:
#Runtime = O(1)
#Space = O(1)