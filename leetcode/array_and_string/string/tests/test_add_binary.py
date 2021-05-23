import pytest

import array_and_string.string.add_binary as prob

class TestAddBinary:
  def test_example1(self):
    a = "11"
    b = "1"
    sum = "100"
    assert prob.addBinary(a, b) == sum
  

  def test_example2(self):
    a = "1010"
    b = "1011"
    sum = "10101"
    assert prob.addBinary(a, b) == sum
  

  def test_empty(self):
    a = ""
    b = ""
    sum = ""
    assert prob.addBinary(a, b) == sum
  

  def test_zero(self):
    a = "0"
    b = "0"
    sum = "0"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_one(self):
    a = "1"
    b = "1"
    sum = "10"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_one_empty(self):
    a = "1101"
    b = ""
    sum = "1101"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_other_empty(self):
    a = ""
    b = "10101"
    sum = "10101"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_one_zero(self):
    a = "0"
    b = "10101"
    sum = "10101"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_other_zero(self):
    a = "101101"
    b = "0"
    sum = "101101"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_all_one(self):
    a = "1111"
    b = "1111"
    sum = "11110"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum
  

  def test_failed_1(self):
    a = "100"
    b = "110010"
    sum = "110110"
    # print(f'Sum = {prob.addBinary(a, b)}')
    assert prob.addBinary(a, b) == sum