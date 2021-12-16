import pytest

import hash_table.happy_number as prob

class TestHappyNumber:
    def test_example1(self):
        n = 19
        res = True
        assert prob.isHappy(n) == res
    
    def test_example2(self):
        n = 2
        res = False
        assert prob.isHappy(n) == res
    
    def test_my1(self):
        n = 100
        print()
        for i in range(1, 101):
            status = "Happy" if prob.isHappy(i) else "Sad"
            print(f"{i} is {status}")