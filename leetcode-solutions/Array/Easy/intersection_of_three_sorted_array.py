class Solution(object):
    def intersection(self, nums1, nums2, nums3):
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        return list(nums1 & nums2 & nums3)

solution = Solution()
print(solution.intersection([1,2,2,1],[2,2],[2]))