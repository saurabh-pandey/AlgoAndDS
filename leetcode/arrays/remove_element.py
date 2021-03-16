#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

def removeElement(nums, val):
    length = len(nums)
    newLen = length
    partitionId = length-1
    # Scan in reverse and set partitionId to skip all contiguous "val" from end
    # for i in range(length - 1, -1, -1):
    #     if nums[i] == val:
    #         newLen -= 1
    #         partitionId -= 1
    #     else:
    #         break
    # print(f'newLen = {newLen}, partitionId = {partitionId}')
    i = 0
    while i < newLen:
        # print(f'\nStart : i = {i}, nums = {nums}, newLen = {newLen}, partitionId = {partitionId}')
        for revId in range(partitionId, -1, -1):
            if nums[revId] == val:
                partitionId -= 1
                newLen -= 1
            else:
                break
        if (partitionId < i):
            break
        # print(f'Mid : i = {i}, nums = {nums}, newLen = {newLen}, partitionId = {partitionId}')
        if nums[i] == val:
            # print(f'  Val found for i = {i}')
            nums[i] = nums[partitionId]
            nums[partitionId] = val
            newLen -= 1
            partitionId -= 1
        # print(f'End: i = {i}, nums = {nums}, newLen = {newLen}, partitionId = {partitionId}')
        i += 1
    return newLen


def test1():
    nums = [3,2,2,3]
    val = 3
    newLen = removeElement(nums, val)
    if newLen == 2:
        print(f'SUCCESS: nums = {nums}')
    else:
        print(f'FAILURE: newLen = {newLen} nums = {nums}')

def test2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    newLen = removeElement(nums, val)
    if newLen == 5:
        print(f'SUCCESS: nums = {nums}')
    else:
        print(f'FAILURE: newLen = {newLen} nums = {nums}')

def test3():
    nums = [0,4,4,0,4,4,4,0,2]
    val = 4
    expectNums = [0,2,0,0]
    newLen = removeElement(nums, val)
    if newLen == 4:
        print(f'SUCCESS: nums = {nums}')
    else:
        print(f'FAILURE: newLen = {newLen} nums = {nums}, expected = {expectNums}')

def run():
    test1()
    test2()
    test3()

run()