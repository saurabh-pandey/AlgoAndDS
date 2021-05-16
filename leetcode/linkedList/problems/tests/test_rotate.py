import pytest

import problems.rotate as prob
import singly_linked_list.operations as sll

class TestRotate:
  def test_example1(self):
    input = [1,2,3,4,5]
    k = 2
    result = [4,5,1,2,3]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  

  def test_example2(self):
    input = [0,1,2]
    k = 4
    result = [2,0,1]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  

  def test_empty(self):
    input = []
    k = 4
    result = []

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  

  def test_single(self):
    input = [1]
    k = 2
    result = [1]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  

  def test_no_rotation(self):
    input = [1,2,3]
    k = 3
    result = [1,2,3]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  
  
  def test_no_rotation_high(self):
    input = [1,2,3]
    k = 300000
    result = [1,2,3]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  

  def test_rotation_high(self):
    input = [1,2,3]
    k = 300001
    result = [3,1,2]

    head = sll.create(input)
    rotatedList = prob.rotateRight(head, k)
    assert sll.toList(rotatedList) == result
  
