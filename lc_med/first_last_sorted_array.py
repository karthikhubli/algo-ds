"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    ret = [-1, -1]
    if len(nums) > 0:
        if len(nums) == 1 and target == nums[0]:
            return [0, 0]
        elif len(nums) == 1 and target != nums[0]:
            return ret
        else:
            print(_get_first_ind(nums, target))
            first_i = _get_first_ind(nums, target)
            if first_i == -1:
                return ret
            i = first_i
            j = first_i
            x = nums[i]
            while i >= 0 and nums[i] == target:
                i -= 1
            y = nums[j]
            while j < len(nums) and nums[j] == target:
                j += 1
            return [i + 1, j - 1]

    return ret


def searchRange_with_bias(nums: List[int], target: int) -> List[int]:
    ret = [-1, -1]
    if len(nums) > 0:
        if len(nums) == 1 and target == nums[0]:
            return [0, 0]
        elif len(nums) == 1 and target != nums[0]:
            return ret
        else:
            left = _bin_search(nums, target, True)
            right = _bin_search(nums, target, False)
            return [left, right]

    return ret


def _get_first_ind(nums, tar) -> int:
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (right + left) // 2
        if tar == nums[mid]:
            return mid
        if tar > nums[mid]:
            # search in the right
            left = mid + 1
        else:
            # search in the right
            right = mid - 1
    return -1


def _bin_search(numbers, tar, leftMost: bool) -> int:
    left = 0
    right = len(numbers) - 1
    ret = -1
    while right >= left:
        mid = (right + left) // 2
        num = numbers[mid]
        if tar < numbers[mid]:
            # search in the right
            right = mid - 1
        if tar > numbers[mid]:
            # search in the right
            left = mid + 1
        else:
            ret = mid
            if leftMost:
                right = mid - 1
            else:
                left = mid + 1
    return ret


if __name__ == '__main__':
    nums = [5,5,7,8,8,10]
    nums = sorted(nums)
    # nums  = [x//2 for x in nums]
    target = 5
    print(f"{nums} || {target} || {len(nums)}\n")
    s1 = searchRange(nums, target)
    print(s1)
    print(nums[s1[0]: s1[1]+1])
    print('---------')
    s2 = searchRange_with_bias(nums, target)
    print(s2)
    print(nums[s2[0]: s2[1]+1])

