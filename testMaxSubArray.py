import random
import time
import matplotlib.pyplot as plt
import maxSubArrayBruteForce
import maxSubArrayDivideConquer
import maxSubArrayDynamicProgramming

def runMaximumSubArray(algo, arr, timeTaken, algoName):
    """Running and timing maximum sub-array problem.
    """
    print "Running Maximum Sub-Array using", algoName, "for size", len(arr)
    startTime = time.time()
    result = algo(arr)
    timeTaken.append(time.time() - startTime)
    return result

def test():
    """Test code to run all algo for randomly generated arrays
    It also times these runs and produces a consolidated plot
    """
    sizes = range(10,200,10)
    tmBF = []
    tmDC = []
    tmDP = []
    for size in sizes:
        arr = [random.randint(-size, size) for i in range(size)]
        resBF = runMaximumSubArray(maxSubArrayBruteForce.maxSubArray,
                                   arr,
                                   tmBF,
                                   "Brute Force")
        resDC = runMaximumSubArray(maxSubArrayDivideConquer.maxSubArray,
                                   arr,
                                   tmDC,
                                   "Divide & Conquer")
        resDP = runMaximumSubArray(maxSubArrayDynamicProgramming.maxSubArray,
                                   arr,
                                   tmDP,
                                   "Dynamic Programming")

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

    plt.plot(sizes, tmBF, 'b--', label = "Brute Force");
    plt.plot(sizes, tmDC, 'r--', label = "Divide & Conquer");
    plt.plot(sizes, tmDP, 'g--', label = "Dynamic Programming");
    plt.legend(loc='upper left')
    plt.title("Maximum Sub-array Problem")
    plt.xlabel("Array size")
    plt.ylabel("Time Taken (sec)")
    plt.grid(True)
    plt.show()
