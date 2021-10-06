import sys
import random
import time
import matplotlib.pyplot as plt
import mergeSort
import selectionSort
import bubbleSort
import insertionSort
import quickSort
import simpleUnintutiveSort

def isSorted(arr):
  """
  Check if the array is sorted.
  """
  return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def runSort(sort, arr, timeTaken, sortingAlgo):
  """
  Running, timing and checking if the array is sorted.
  """
  localArr = arr[:]
  print(f"Running {sortingAlgo} for size {len(localArr)}")
  startTime = time.time()
  sort(localArr)
  timeTaken.append(time.time() - startTime)
  if not isSorted(localArr):
    print(f"Array is NOT correctly sorted by {sortingAlgo}") 

def test():
  """
  Test code to run all sorting algo for randomly generated arrays.
  It also times these runs and produces a consolidated plot
  """
  sizes = range(100,1000,50)
  tmMS = [] # Merge sort timing
  tmIS = [] # Insertion sort timing
  tmBS = [] # Bubble sort timing
  tmSS = [] # Selection sort timimg
  tmQS = [] # Quick sort timing
  tmSU = [] # Simple Unintutive sort timing
  for size in sizes:
    arr = [random.randint(-size, size) for i in range(size)]
    runSort(mergeSort.sort, arr, tmMS, "Merge Sort")
    runSort(insertionSort.sort, arr, tmIS, "Insertion Sort")
    runSort(selectionSort.sort, arr, tmSS, "Selection Sort")
    runSort(bubbleSort.sort, arr, tmBS, "Bubble Sort")
    runSort(quickSort.sort, arr, tmQS, "Quick Sort")
    runSort(simpleUnintutiveSort.sort, arr, tmSU, "Simple Unintutive Sort")

  plt.plot(sizes, tmMS, 'k--', label = "Merge Sort")
  plt.plot(sizes, tmIS, 'r-.', label = "Insertion Sort")
  plt.plot(sizes, tmSS, 'b:', label = "Selection Sort")
  plt.plot(sizes, tmBS, 'g--', label = "Bubble Sort")
  plt.plot(sizes, tmQS, '--', label = "Quick Sort", color='orange')
  plt.plot(sizes, tmSU, 'o-', label = "Simple Unintutive Sort")
  plt.legend(loc='upper left')
  plt.title("Sorting Performance Comparison")
  plt.xlabel("Array size")
  plt.ylabel("Time Taken (sec)")
  plt.grid(True)
  plt.show()
