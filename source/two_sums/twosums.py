from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if num1 + num2 == target:
                return [i, i+j+1]