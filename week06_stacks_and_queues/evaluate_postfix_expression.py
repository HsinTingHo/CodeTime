# Problem 1 - Evaluate Postfix expression
# Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators '+', '*', '-' and '/'.

# Example:

# Input: "5 1 2  +  4  * +  3  -"
# Output: 14

# The expression is evaluated as follows:
#     5 3 4 * + 3 -
#     5 12 + 3 -
#     17 3 -
#     14

#Understand
# What to do when the the input is an invalid expr?
# edge case
# Input: "5 1 2  +  4  * +  3  -"
# Output: 14

#Match
#Stack

#Plan:
#initiate a stack (arr)
#split the input by whitespace into char_arr
#loop through char_arr
#.   if element is a number, put into  stack
#.   if element is an operator and there are more than 1 element in stack
#.      pop two number from stack and evaluate
#.      push evaluation back to stack
#.   else, print "invalid expression" and return none
#if stack has exactly 1 element, pop and return the element
#else, print "invalid expression" and return none 

def evaluate_postfix_expression(expr):
  if expr is not None:
    char_arr = expr.split()
    stack = []
    for char in char_arr:
      if char.isdigit():
        stack.append(char)
      else:
        if len(stack) > 1:
          num2 = stack.pop()
          num1 = stack.pop()
          sum = str(eval(num1+char+num2))
          
          stack.append(sum)
        else:
          print('Invalid Expression')
          return
    if len(stack) == 1:
      return stack.pop()
    else:
      print('Invalid Expression')
      return
          
#evaluation
#Runtime = O(n)
#space = O(n)

#*************************
# total time: 37m 43s
#*************************
