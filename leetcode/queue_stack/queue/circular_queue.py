#URL: https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/
#Description
"""
Design your implementation of the circular queue. The circular queue is a linear data structure in 
which the operations are performed based on FIFO (First In First Out) principle and the last 
position is connected back to the first position to make a circle. It is also called "Ring Buffer".
One of the benefits of the circular queue is that we can make use of the spaces in front of the 
queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if 
there is a space in front of the queue. But using the circular queue, we can use the space to store 
new values.

Implementation the MyCircularQueue class:
MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation 
is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is 
successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming 
language. 


Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4


Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""
import pdb

class CircularQueue:
  def __init__(self, k):
    self.data = [None for i in range(k)]
    self.capacity = k
    self.start = -1
    self.end = -1
  

  def isEmpty(self):
    if self.start == -1 and self.end == -1:
      return True
    return False
  

  def isFull(self):
    if self.isEmpty():
      return False
    nextEnd = self.end + 1
    nextEnd %= self.capacity
    if nextEnd != self.start:
      return False
    return True

  
  def front(self):
    if self.isEmpty():
      return -1
    return self.data[self.start]
  

  def rear(self):
    if self.isEmpty():
      return -1
    return self.data[self.end]
  

  def enQueue(self, value):
    # pdb.set_trace()
    if self.isFull():
      return False
    if self.isEmpty():
      self.start = 0
    self.end += 1
    self.end %= self.capacity
    self.data[self.end] = value
    return True
  

  def deQueue(self):
    if self.isEmpty():
      return False
    self.data[self.start] = None
    if self.start == self.end:
      self.start = -1
      self.end = -1
    else:
      self.start += 1
      self.start %= self.capacity
    return True
