#Description
"""
Given a capacity of knapsack W and a number of items N. Each item has a weight w_i and some value v_i. Find the items that maximize the value in the knapsack.

Example:
W = 6, N = 4
v1 = 3, w1 = 4
v2 = 2, w2 = 3
v3 = 4, w3 = 2
v4 = 4, w4 = 3

Optimal value = 8 and items = [Item 3 and Item 4]

NOTE: This was the second problem discussed in the DP part of Tim's algo-2 course
"""
def solveKnapsack(W, items):
    # print()
    N = len(items)
    A = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    # print(A)
    for i in range(1, N + 1):
        (v_i, w_i) = items[i - 1]
        for w in range(W + 1):
            rem_cap = w - w_i
            # print(i, w, rem_cap)
            if rem_cap < 0:
                A[i][w] = A[i - 1][w]
            else:
                A[i][w] = max(A[i - 1][w], A[i - 1][rem_cap] + v_i)
    # for i in range(len(A) - 1, -1, -1):
    #     print(A[i])
    i = len(A) - 1
    j = len(A[i]) - 1
    selected_items = []
    while i >= 1 and j >= 0:
        (v_i, w_i) = items[i - 1]
        rem_cap = j - w_i
        if A[i][j] == 0:
            break
        elif A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i - 1][rem_cap] + items[i - 1][0]:
            selected_items.append(items[i - 1])
            i -= 1
            j = rem_cap
    # print(selected_items)
    return selected_items