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