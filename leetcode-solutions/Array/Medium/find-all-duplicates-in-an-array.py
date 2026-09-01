'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
 
Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.'''

class Solution(object):
    def findDuplicates(self, nums):
        from collections import Counter
        nums=sorted(nums)
        f = Counter(nums)
        r = []
        for i in range (1, len(nums)+1):
            if f[i] >1:
                r.append(i)
        return r

solution = Solution()
print(solution.findDuplicates([4,3,2,7,8,2,3,1]))