import pytest

import queue_stack.problems.flood_fill as prob

class TestFloodFill:
  def test_example1(self):
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    res = [[2,2,2],[2,2,0],[2,0,1]]
    assert prob.floodFill(image, sr, sc, newColor) == res
  

  def test_example2(self):
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    res = [[2,2,2],[2,2,2]]
    assert prob.floodFill(image, sr, sc, newColor) == res