import pytest

from queue_stack.stack.min_stack import MinStack

class TestCircularQueue:
  def test_example1(self):
    myMinStack = MinStack()
    assert myMinStack.isEmpty() == True
    assert myMinStack.pop() == False
    assert myMinStack.top() == False
    assert myMinStack.getMin() == False

    myMinStack.push(-2)
    assert myMinStack.isEmpty() == False
    assert myMinStack.top() == -2
    assert myMinStack.getMin() == -2

    myMinStack.push(0)
    assert myMinStack.isEmpty() == False
    assert myMinStack.top() == 0
    assert myMinStack.getMin() == -2

    myMinStack.push(-3)
    assert myMinStack.isEmpty() == False
    assert myMinStack.top() == -3
    assert myMinStack.getMin() == -3

    assert myMinStack.pop() == -3
    assert myMinStack.isEmpty() == False
    assert myMinStack.top() == 0
    assert myMinStack.getMin() == -2
  

  def test_my_example1(self):
    myMinStack = MinStack()

    myMinStack.push(-2)
    myMinStack.push(0)
    myMinStack.push(-3)
    myMinStack.pop()
    
    assert myMinStack.pop() == 0
    assert myMinStack.isEmpty() == False
    assert myMinStack.top() == -2
    assert myMinStack.getMin() == -2
    
    assert myMinStack.pop() == -2
    assert myMinStack.isEmpty() == True
    assert myMinStack.top() == False
    assert myMinStack.getMin() == False

    assert myMinStack.pop() == False
