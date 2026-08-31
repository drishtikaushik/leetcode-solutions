'''
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''

class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        freq = Counter(nums)
        r = []
        for i in range (len(nums)):
            if freq[nums[i]]>(len(nums)/3):
                for j in range (len(r)):
                    if r[j]==nums[i]:
                        break
                else:
                    r.append(nums[i])
        return r

solution = Solution()
print(solution.majorityElement([3,2,3]))