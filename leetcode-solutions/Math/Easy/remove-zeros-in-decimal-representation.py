'''You are given a positive integer n.
Return the integer obtained by removing all zeros from the decimal representation of n.

Example 1:
Input: n = 1020030
Output: 123
Explanation:
After removing all zeros from 1020030, we get 123.

Example 2:
Input: n = 1
Output: 1
Explanation:
1 has no zero in its decimal representation. Therefore, the answer is 1.


Constraints:
1 <= n <= 10^15'''

class Solution(object):
    def removeZeros(self, n):
        n = str(n)
        r =""
        for i in range (len(n)):
            if n[i]!="0":
                r+=(n[i])
        return int(r)

solution=Solution()
print(solution.removeZeros(1020030))

