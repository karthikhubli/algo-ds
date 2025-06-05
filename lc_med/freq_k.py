'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if len(nums) == 0:
        return None
    count_dict = dict()
    for i in range (len(nums)):
        if nums[i] in count_dict.keys():
            temp = count_dict[nums[i]]
            count_dict[nums[i]] = temp+1
        else:
            count_dict[nums[i]] = 1

    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_keys = list(sorted_dict.keys())
    return sorted_keys[:k]

def topKFrequent_heap(nums: List[int], k: int) -> List[int]:
    count_dict = {}
    for i in nums:
        count_dict[i] = count_dict.get(i, 0) + 1
    k_heap = []
    for x, f in count_dict.items():
        heapq.heappush(k_heap, (f, x))
        if len(k_heap) > k:
            heapq.heappop(k_heap)
    result = []  # Initialize an empty list to store the results
    for _count, elm in k_heap:  # Iterate through the elements in the heap h
        result.append(elm)  # Append the element (the second item of each tuple) to the result list
    return result  # Return the list of elements


if __name__ == '__main__':
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(topKFrequent_heap(nums, k))