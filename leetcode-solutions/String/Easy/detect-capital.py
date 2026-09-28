'''We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.'''


class Solution(object):
    def detectCapitalUse(self, word):
        if len(word) == 1:
            return True

        if 65 <= ord(word[0]) <= 90:
            f = 1
        else:
            f = 0

        if f==1:
            p = 0

            for i in range(1, len(word)):
                if 97 <= ord(word[i]) <= 122:
                    p += 0
                elif 65 <= ord(word[i]) <= 90:
                    p += 1

            if p==(len(word)-1) or p==0:
                return True
            else:
                return False

        if f==0:
            p = 0

            for i in range(1, len(word)):
                if 97 <= ord(word[i]) <= 122:
                    p += 0
                elif 65 <= ord(word[i]) <= 90:
                    return False
            return True


sol = Solution()
print(sol.detectCapitalUse("FlaG"))