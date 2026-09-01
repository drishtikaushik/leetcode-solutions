class Solution(object):
    def findDisappearedNumbers(self, nums):
        from collections import Counter
        f = Counter(nums)
        o = []
        n = 1
        while n<=len(nums):
            if n not in f:
                o.append(n)
            n+=1
        return o

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))