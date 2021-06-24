import pytest

import queue_stack.queue.num_islands as prob

class TestNumIslands:
  def test_example1(self):
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    res = 1
    assert prob.numIslands(grid) == res
  

  def test_example2(self):
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    res = 3
    assert prob.numIslands(grid) == res
  

  def test_empty(self):
    grid = []
    res = 0
    assert prob.numIslands(grid) == res
  

  def test_empty1(self):
    grid = [[]]
    res = 0
    assert prob.numIslands(grid) == res
  

  def test_my_example1(self):
    grid = [["1"]]
    res = 1
    assert prob.numIslands(grid) == res
  

  def test_my_example2(self):
    grid = [["0"]]
    res = 0
    assert prob.numIslands(grid) == res
  

  def test_all_land(self):
    grid = [["1","1","1"],
            ["1","1","1"]]
    res = 1
    assert prob.numIslands(grid) == res
  

  def test_all_water(self):
    grid = [["0","0","0"],
            ["0","0","0"]]
    res = 0
    assert prob.numIslands(grid) == res
  

  def test_diagonal(self):
    grid = [["1","0","0","0"],
            ["0","1","0","0"],
            ["0","0","1","0"],
            ["0","0","0","1"]]
    res = 4
    assert prob.numIslands(grid) == res