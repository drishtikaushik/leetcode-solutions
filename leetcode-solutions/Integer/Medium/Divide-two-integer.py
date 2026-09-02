class Solution(object):
    def divide(self, dividend, divisor):
        r = dividend/divisor
        if r>0:
            return r
        elif r<0:
            return r+1

solution = Solution()
print(solution.divide(4, 5))