#URL: https://www.geeksforgeeks.org/sequence-alignment-problem/
#Description
"""
Given as an input two strings, X = x1x2...xm, and Y = y1y2...yn, output the alignment of the 
strings, character by character, so that the net penalty is minimised. The penalty is calculated 
as: 
1. A penalty of p_gap  occurs if a gap is inserted between the string. 
2. A penalty of p_xy   occurs for mis-matching the characters of X and Y.

Examples:
Input : X = CG, Y = CA, p_gap = 3, p_xy = 7
Output : X = CG_, Y = C_A, Total penalty = 6

Input : X = AGGGCT, Y = AGGCA, p_gap = 3, p_xy = 2
Output : X = AGGGCT, Y = A_GGCA, Total penalty = 5

Input : X = CG, Y = CA, p_gap = 3, p_xy = 5
Output : X = CG, Y = CA, Total penalty = 5
"""

def getMinPenaltyAlignment(X, Y, p_gap, p_xy):
    m = len(X)
    n = len(Y)
    A = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # Initialize
    for i in range(m + 1):
        A[i][0] = i*p_gap
    for j in range(n + 1):
        A[0][j] = j*p_gap
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(A[i- 1][j] + p_gap, A[i][j - 1] + p_gap, A[i- 1][j - 1] + p_xy)
    # print()
    # for row in A:
        # print(row)
    
    # Reconstruct
    matchedX = []
    matchedY = []
    i = m
    j = n
    while i >= 1 and j >= 1:
        if (A[i][j] == A[i - 1][j - 1]) and (X[i - 1] == Y[j - 1]):
            matchedX.append(X[i - 1])
            matchedY.append(Y[j - 1])
            i -= 1
            j -= 1
        elif A[i][j] == A[i - 1][j - 1] + p_xy:
            matchedX.append(X[i - 1])
            matchedY.append(Y[j - 1])
            i -= 1
            j -= 1
        elif A[i][j] == A[i][j - 1] + p_gap:
            matchedX.append("_")
            matchedY.append(Y[j - 1])
            j -= 1
        elif A[i][j] == A[i - 1][j] + p_gap:
            matchedX.append(X[i - 1])
            matchedY.append("_")
            i -= 1
    while i >= 1:
        matchedX.append(X[i - 1])
        i -= 1
    while j >= 1:
        matchedY.append(Y[j - 1])
        j -= 1
    lenX = len(matchedX)
    lenY = len(matchedY)
    if lenX < lenY:
        matchedX.extend((lenY - lenX) *["_"])
    elif lenX > lenY:
        matchedY.extend((lenX - lenY) *["_"])
    matchedX.reverse()
    matchedY.reverse()
    # print(matchedX)
    # print(matchedY)
    return (A[m][n], ''.join(matchedX), ''.join(matchedY))