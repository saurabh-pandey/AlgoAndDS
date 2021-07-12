import pytest

from queue_stack.problems.stack_using_queue import MyStack

class TestStackUsingQueue:
  def test_example1(self):
    myStack = MyStack()
    assert myStack.empty() == True
    myStack.push(1)
    assert myStack.empty() == False
    myStack.push(2)
    assert myStack.empty() == False
    assert myStack.top() == 2
    assert myStack.pop() == 2
    assert myStack.empty() == False
  

  def test_my_example1(self):
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    myStack.pop()
    assert myStack.top() == 1
    assert myStack.pop() == 1
    assert myStack.empty() == True
    myStack.push(1)
    assert myStack.empty() == False
    assert myStack.top() == 1
    assert myStack.pop() == 1
    assert myStack.empty() == True