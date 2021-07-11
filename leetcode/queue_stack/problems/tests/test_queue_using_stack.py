import pytest

from queue_stack.problems.queue_using_stack import MyQueue

class TestQueueUsingStack:
  def test_example1(self):
    myQueue = MyQueue()
    assert myQueue.empty() == True
    myQueue.push(1)
    assert myQueue.empty() == False
    myQueue.push(2)
    assert myQueue.empty() == False
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert myQueue.empty() == False