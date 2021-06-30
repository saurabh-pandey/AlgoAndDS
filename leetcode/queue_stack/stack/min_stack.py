#URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
#Description
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack:
  def __init__(self):
    self._data = []
    self._minId = None

  
  def push(self, val):
    self.__checkData()
    self._data.append(val)
    if self._minId is None:
      self._minId = 0
    else:
      self._minId = self._minId if self._data[self._minId] < val else (len(self._data) - 1)
    

  def isEmpty(self):
    self.__checkData()
    return len(self._data) == 0
  
  
  def pop(self):
    if self.isEmpty():
      return False
    
    dataSz = len(self._data)
    if dataSz == 1:
      self._minId = None
      return self._data.pop()
    
    # Update minId before popping the last element if needed
    if self._minId == dataSz - 1:
      self._minId = 0
      for i in range(1, dataSz - 1):
        if self._data[i] < self._data[self._minId]:
          self._minId = i
    return self._data.pop()

  
  def top(self):
    if self.isEmpty():
      return False
    
    return self._data[len(self._data) - 1]
  
  
  def getMin(self):
    if self.isEmpty():
      return False
    
    return self._data[self._minId]


  def __checkData(self):
    if len(self._data) == 0:
      assert self._minId is None 
