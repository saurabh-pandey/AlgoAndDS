'''
Node of a N-ary tree
'''

class Node:
  def __init__(self, val, children=None):
    self.val = val
    if children is None:
      self.children = []
    else:
      self.children = children
