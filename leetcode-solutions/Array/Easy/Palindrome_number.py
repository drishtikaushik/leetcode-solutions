'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution(object):
    def isPalindrome(self, x):
        z = [int(digit) for digit in str(abs(x))]
        y = z[::-1]
        print(z)
        print(y)
        if z == y and x>=0:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(121))