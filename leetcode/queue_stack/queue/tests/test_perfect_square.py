import pytest

import queue_stack.queue.perfect_square as prob

import pdb

class TestPerfectSquare:
    def test_my_example1(self):
        # print()
        # pdb.set_trace()
        # print(prob.numSquares(13))
        answers = {1:1, 2:2, 3:3, 4:1, 5:2, 6:3, 7:4, 8:2, 9:1, 10:2, 11:3, 12:3, 13:2, 14:3,
                   15:4, 16:1}
        for num, res in answers.items():
            assert prob.numSquares(num) == res

  
    def test_example1(self):
      n = 12
      res = 3
      assert prob.numSquares(n) == res