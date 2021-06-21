import pytest

import queue_stack.queue.circular_queue as q

class TestCircularQueue:
  def test_example1(self):
    myQueue = q.CircularQueue(3)
    assert myQueue.isEmpty() == True
    assert myQueue.isFull() == False
    assert myQueue.front() == -1
    assert myQueue.rear() == -1
    assert myQueue.enQueue(1) == True
    assert myQueue.enQueue(2) == True
    assert myQueue.enQueue(3) == True
    assert myQueue.enQueue(4) == False
    assert myQueue.rear() == 3
    assert myQueue.isFull() == True
    assert myQueue.deQueue() == True
    assert myQueue.enQueue(4) == True
    assert myQueue.rear() == 4
  

  def test_example2(self):
    myQueue = q.CircularQueue(3)
    
    assert myQueue.enQueue(1) == True
    assert myQueue.isEmpty() == False
    assert myQueue.isFull() == False
    assert myQueue.rear() == 1
    assert myQueue.front() == 1
    
    assert myQueue.enQueue(2) == True
    assert myQueue.isEmpty() == False
    assert myQueue.isFull() == False
    assert myQueue.rear() == 2
    assert myQueue.front() == 1
    
    assert myQueue.enQueue(3) == True
    assert myQueue.isEmpty() == False
    assert myQueue.isFull() == True
    assert myQueue.rear() == 3
    assert myQueue.front() == 1
    
    assert myQueue.enQueue(4) == False
    assert myQueue.rear() == 3
    assert myQueue.front() == 1

    assert myQueue.deQueue() == True
    assert myQueue.rear() == 3
    assert myQueue.front() == 2
    assert myQueue.isEmpty() == False
    assert myQueue.isFull() == False
    
    assert myQueue.deQueue() == True
    assert myQueue.rear() == 3
    assert myQueue.front() == 3
    assert myQueue.isEmpty() == False
    assert myQueue.isFull() == False

    assert myQueue.deQueue() == True
    assert myQueue.rear() == -1
    assert myQueue.front() == -1
    assert myQueue.isEmpty() == True
    assert myQueue.isFull() == False

    assert myQueue.deQueue() == False
    assert myQueue.rear() == -1
    assert myQueue.front() == -1
    assert myQueue.isEmpty() == True
    assert myQueue.isFull() == False
  

  def test_lc_run1(self):
    myQueue = q.CircularQueue(4)
    
    assert myQueue.enQueue(3) == True
    assert myQueue.front() == 3
    assert myQueue.isFull() == False
    assert myQueue.enQueue(7) == True
    assert myQueue.enQueue(2) == True
    assert myQueue.enQueue(5) == True
    assert myQueue.deQueue() == True
    assert myQueue.enQueue(4) == True
    assert myQueue.enQueue(2) == False
    assert myQueue.isEmpty() == False
    assert myQueue.rear() == 4