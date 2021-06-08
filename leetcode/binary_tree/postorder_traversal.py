#URL: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
#Description
"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [1]
Output: [1]


Example 4:

Input: root = [1,2]
Output: [2,1]


Example 5:

Input: root = [1,null,2]
Output: [2,1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
def postorderRecursiveImpl(node, postorderList):
  if node.left is not None:
    postorderRecursiveImpl(node.left, postorderList)
  if node.right is not None:
    postorderRecursiveImpl(node.right, postorderList)
  postorderList.append(node.val)


def postorderRecursive(root):
  if root is None:
    return []
  
  postorderList = []
  postorderRecursiveImpl(root, postorderList)
  return postorderList


def postorderIterative(root):
  postorderList = []
  nodes = []
  prevNode = None
  node = root
  while len(nodes) > 0 or node is not None:
    if node is not None:
      nodes.append(node)
      node = node.left
    else:
      currNode = nodes[-1]
      if currNode.right is not None and prevNode != currNode.right:
        node = currNode.right
      else:
        postorderList.append(currNode.val)
        prevNode = nodes.pop()
  return postorderList


def postorderTraversal(root, doRecursive=True):
  if doRecursive:
    return postorderRecursive(root)
  else:
    return postorderIterative(root)
