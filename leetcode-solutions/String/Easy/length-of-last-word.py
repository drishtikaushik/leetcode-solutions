'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.'''


class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s)>0:
            if s[-1]== ' ':
                s=s[ :-1]
            elif s[-1]!= ' ':
                end = len(s)
                strt = -1
                for i in range (len(s)) :
                    while s[-i] != ' ':
                        strt-=1
                r = end - strt
        return r

sol = Solution()
print(sol.lengthOfLastWord("Hello World")) # Output: 5