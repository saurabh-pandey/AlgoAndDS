#Description
"""
Find maximum weight independent set of a path graph.
A path graph is a set of vertices in a line. Each vertex has a non-negative weight associated with 
it.
An independent set in path graph is set of vertices with no adjacent pairs. In general it is a set 
of vertices with no edges between them.
The problem is to find amongst all the independent set the one set that maximizes the weight.

Example:
v = [1, 4, 5, 4]
v is a path graph with 4 vertices
All independent sets = {}, {v0}, {v1}, {v2}, {v3}, {v0, v2}, {v0, v3}, {v1, v3}
Thus a total of 8 IS
Now the IS that maximizes the weight is {v1, v3} = {4, 4} = 8

NOTE: This was the first problem discussed in Tim's algo-2 course
"""

def maxWtIS(nums):
    # Filter empty case
    if not nums:
        return []
    
    # Fill the max weights
    A = [0 for _ in range(len(nums) + 1)]
    A[0] = 0
    A[1] = nums[0]
    for i in range(2, len(A)):
        A[i] = max(A[i - 1], A[i - 2] + nums[i - 1])
    # Use max weights to fill the IS
    S = []
    i = len(A) - 1
    while i >= 1:
        if i == 1:
            S.append(nums[i - 1])
            i -= 2
        elif A[i - 1] >= A[i - 2] + nums[i - 1]:
            i -= 1
        else:
            S.append(nums[i - 1])
            i -= 2
    return S
    