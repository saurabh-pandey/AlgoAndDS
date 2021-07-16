import pytest

import queue_stack.problems.keys_rooms as prob

class TestKeysAndRooms:
  def test_example1(self):
    rooms = [[1],[2],[3],[]]
    res = True
    assert prob.canVisitAllRooms(rooms) == res
  

  def test_example2(self):
    rooms = [[1,3],[3,0,1],[2],[0]]
    res = False
    assert prob.canVisitAllRooms(rooms) == res