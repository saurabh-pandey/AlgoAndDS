#URL: https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/
#Description
"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should 
support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from 
front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using 
a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""

class MyStack:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queues = [[],[]]
    self.push_queue_id = 0
    self.pop_queue_id = 1


  def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    if len(self.queues[self.push_queue_id]) == 1:
      self.queues[self.pop_queue_id].append(self.queues[self.push_queue_id].pop(0))
    assert len(self.queues[self.push_queue_id]) == 0
    self.queues[self.push_queue_id].append(x)


  def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    assert len(self.queues[self.push_queue_id]) == 1
    poppedItem = self.queues[self.push_queue_id].pop(0)
    while len(self.queues[self.pop_queue_id]) > 1:
      self.queues[self.push_queue_id].append(self.queues[self.pop_queue_id].pop(0))
    assert len(self.queues[self.pop_queue_id]) <= 1
    prev_push_id = self.push_queue_id
    self.push_queue_id = self.pop_queue_id
    self.pop_queue_id = prev_push_id
    return poppedItem


  def top(self) -> int:
    """
    Get the top element.
    """
    assert len(self.queues[self.push_queue_id]) == 1
    return self.queues[self.push_queue_id][0]


  def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    isPushQueueEmpty = len(self.queues[self.push_queue_id]) == 0
    isPopQueueEmpty = len(self.queues[self.pop_queue_id]) == 0
    return isPushQueueEmpty and isPopQueueEmpty