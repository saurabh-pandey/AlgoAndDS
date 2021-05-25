import pytest

import array_and_string.string.longest_common_prefix as prob

class TestLongestCommonPrefix:
  def test_example1(self):
    strs = ["flower","flow","flight"]
    result = "fl"
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_example2(self):
    strs = ["dog","racecar","car"]
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_empty(self):
    strs = []
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_single(self):
    strs = ["abc"]
    result = "abc"
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_all_match(self):
    strs = ["abc", "abc", "abc", "abc"]
    result = "abc"
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_one_empty(self):
    strs = ["abc", "abc", "", "abc"]
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_last_no_match(self):
    strs = ["abc", "abc", "abc", "def"]
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_decreasing(self):
    strs = ["abc", "ab", "a"]
    result = "a"
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  
  
  def test_increasing(self):
    strs = ["a", "ab", "abc", "abcd"]
    result = "a"
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  

  def test_decreasing_empty(self):
    strs = ["abc", "ab", "a", ""]
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result
  
  
  def test_increasing_empty(self):
    strs = ["", "a", "ab", "abc", "abcd"]
    result = ""
    # print(f'Prefix = {prob.longestCommonPrefix(strs)}')
    assert prob.longestCommonPrefix(strs) == result