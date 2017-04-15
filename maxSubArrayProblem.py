import sys
import random
import time
import matplotlib.pyplot as plt

def maxSubArrayBF(arr):
    """Brute-Force algo [O(n^2)] for maximum subarray problem"""
    maxSubArr = []
    maxSum = -sys.maxint -1
    for start in range(len(arr)):
        for end in range(start+1, (len(arr) +1)):
            subArr = arr[start:end]
            subArrSum = sum(subArr)
            if (maxSum < subArrSum):
                maxSum = subArrSum
                maxSubArr = subArr
    return (maxSum, maxSubArr)

def subArraySum(arr):
    """A helper function for computing a part of cross-over case"""
    maxSum = -sys.maxint -1
    sumSoFar = 0
    subArr = []
    for i in range(len(arr)):
        sumSoFar += arr[i]
        if (maxSum < sumSoFar):
            maxSum = sumSoFar
            subArr = arr[:i+1]
    return (maxSum, subArr)

def maxSubArrayCrossOver(left, right):
    """Computes cross-over case for maximum subarray problem.
    Used internally by Divide & Conquer algo.
    """
    maxLeft = subArraySum(list(reversed(left)))
    maxLeft[1].reverse()
    maxRight = subArraySum(right)
    return (maxLeft[0] + maxRight[0], maxLeft[1] + maxRight[1])

def maxSubArrayDC(arr):
    """Divide & Conquer algo [O(nlgn)] for maximum subarray problem"""
    size = len(arr)
    if (size == 1):
        return (arr[0], arr)
    newSize = size/2

    leftSubArr  = arr[:newSize]
    rightSubArr = arr[newSize:]

    leftResult   = maxSubArrayDC(leftSubArr)
    rightResult  = maxSubArrayDC(rightSubArr)
    crossOverRes = maxSubArrayCrossOver(leftSubArr, rightSubArr)
    return max(leftResult, rightResult, crossOverRes)

def maxSubArrayDP(arr):
    """Dynamic Programming algo [O(n)] for maximum subarray problem"""
    maxSubArr = []
    maxSum = -sys.maxint -1
    sumSoFar = 0
    subArrSoFar = []
    for i in arr:
        sumSoFar += i
        subArrSoFar.append(i)
        if (maxSum < sumSoFar):
            maxSum = sumSoFar
            maxSubArr = subArrSoFar[:]
        if (sumSoFar <= 0):
            sumSoFar = 0
            del subArrSoFar[:]
    return (maxSum, maxSubArr)

def test():
    """Test code to run all algo for randomly generated arrays
    It also times these runs and produces a consolidated plot
    """
    sizes = range(10,1000,10)
    tmBF = []
    tmDC = []
    tmDP = []
    for size in sizes:
        arr = [random.randint(-size, size) for i in range(size)]
        print "Running BF for size", size
        startBF = time.time()
        resBF = maxSubArrayBF(arr)
        endBF= time.time()
        timeBF = endBF - startBF
        tmBF.append(timeBF)

        print "Running DC for size", size
        startDC = time.time()
        resDC = maxSubArrayDC(arr)
        endDC= time.time()
        timeDC = endDC - startDC
        tmDC.append(timeDC)

        print "Running DP for size", size
        startDP = time.time()
        resDP = maxSubArrayDP(arr)
        endDP = time.time()
        timeDP = endDP - startDP
        tmDP.append(timeDP)

        if (resBF[0] != resDC[0]):
            print "Error: DC & BF mismatch"
            print arr
            print resBF
            print resDC
        if (resBF[0] != resDP[0]):
            print "Error: DP & BF mismatch"
            print arr
            print resBF
            print resDP

    plt.plot(sizes, tmBF, 'r--', sizes, tmDC, 'b--', sizes, tmDP, 'g--')
    plt.grid(True)
    plt.show()
