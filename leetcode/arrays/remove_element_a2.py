from typing import List

def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0
    
    s = 0
    e = len(nums) - 1
    while s < e:
        if nums[s] == val:
            while nums[e] == val and e > s:
                e -= 1
            if e == s:
                break
            nums[s] = nums[e]
            nums[e] = val
            e -= 1
        if e == s:
            break
        s += 1
    assert s == e, "Start and End ptr should match here"
    if nums[s] == val:
        return s
    else:
        return s + 1

