#URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
#Description
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would 
always evaluate to a result, and there will not be any division by zero operation.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9


Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6


Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
def evalRPN(tokens):
  evalStack = []
  for t in tokens:
    if t == "+":
      num1 = evalStack.pop()
      num2 = evalStack.pop()
      evalStack.append(num2 + num1)
    elif t == "-":
      num1 = evalStack.pop()
      num2 = evalStack.pop()
      evalStack.append(num2 - num1)
    elif t == "*":
      num1 = evalStack.pop()
      num2 = evalStack.pop()
      evalStack.append(num2 * num1)
    elif t == "/":
      num1 = evalStack.pop()
      num2 = evalStack.pop()
      evalStack.append(int(num2 / num1))
    else:
      evalStack.append(int(t))
  assert len(evalStack) == 1
  return evalStack[0]