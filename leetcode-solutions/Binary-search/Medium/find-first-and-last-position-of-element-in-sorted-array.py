'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
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
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
'''

class Solution(object):
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]

        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            i = (low + high) // 2

            if nums[i] == target:
                first = i
                high = i - 1
            elif nums[i] < target:
                low = i + 1
            else:
                high = i - 1

        if first == -1:
            return [-1, -1]

        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            i = (low + high) // 2

            if nums[i] == target:
                last = i
                low = i + 1
            elif nums[i] < target:
                low = i + 1
            else:
                high = i - 1

        return [first, last]