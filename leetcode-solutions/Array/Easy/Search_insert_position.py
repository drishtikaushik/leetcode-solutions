'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 1:
            if nums[0] < target:
                return (1)
            elif nums[0] > target:
                return (0)
            else:
                return (0)
        else:
            for i in range (len(nums)-1):
                if nums[i] == target:
                    return (i)
                elif nums[i] < target < nums[i+1]:
                    return (i+1)
                elif nums[-1] < target:
                    return (len(nums))
                elif nums[-1] == target:
                    return (len(nums)-1)
                else:
                    if nums[0] > target:
                        return(0)

solution = Solution()
print(solution.searchInsert([1,3], 3))