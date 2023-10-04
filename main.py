from typing import List

def twoSum( nums: List[int], target: int) -> List[int]:
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            if nums[i]+nums[j] is target:
                return [i,j]
    return