import pytest

import queue_stack.queue.open_lock as prob

class TestOpenLock:
  def test_example1(self):
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    res = 6
    assert prob.openLock(deadends, target) == res