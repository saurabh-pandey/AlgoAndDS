#Description
"""
Given some keys [1,2,...,n] and the keys' search probabilities = [p1, p2, ..., Pn]
Now return the most optimal Binary Search Tree (BST) such that the average cost to query the nodes 
in the tree is minimized.

Assume that the query node is always in the tree. So no failed queries.

Example 1
For nodes 1,2,3,4 with probabilities = [2, 23, 73, 1]. The optimal BST is has root is 3 left child 
is 2 and right is 4. Left child to 2 is 1


Example 2
Similar example, For nodes 1,2,3,4 with probabilities = [1, 34, 33, 32]. Optimal BST in this case 
is same as above example.


Example 3
keys[] = {10, 12}, freq[] = {34, 50}. Frequency is the number of searches for each node. Optimal BST is root as 12.


Example 4
keys[] = {10, 12, 20}, freq[] = {34, 8, 50}. Optimal BST has 20 as root 10 as it left child. 12 is 
the right child of 10.

NOTE: This was the third problem discussed in the DP part of Tim's algo-2 course
"""