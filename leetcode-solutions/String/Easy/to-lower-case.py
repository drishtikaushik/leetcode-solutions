'''Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
 
Constraints:
1 <= s.length <= 100
s consists of printable ASCII characters.'''

class Solution(object):
    def toLowerCase(self, s):
        r= ""
        for i in range (len(s)):
            if 65<=ord(s[i])<=90:
                c = ord(s[i]) + 32
                l = chr(c)
                r+=l
            else:
                r+=s[i]
        return r

sol = Solution()
print(sol.toLowerCase("Hello"))