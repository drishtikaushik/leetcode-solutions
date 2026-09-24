'''Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31st, 2019.'''

class Solution(object):
    def dayOfYear(self, date):
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        feb = 28

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            feb = 29

        if month == 1:
            return day
        elif month == 2:
            return 31 + day
        elif month == 3:
            return 31 + feb + day
        elif month == 4:
            return 31 + feb + 31 + day
        elif month == 5:
            return 31 + feb + 31 + 30 + day
        elif month == 6:
            return 31 + feb + 31 + 30 + 31 + day
        elif month == 7:
            return 31 + feb + 31 + 30 + 31 + 30 + day
        elif month == 8:
            return 31 + feb + 31 + 30 + 31 + 30 + 31 + day
        elif month == 9:
            return 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + day
        elif month == 10:
            return 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
        elif month == 11:
            return 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
        else:
            return 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day



sol = Solution()
print(sol.dayOfYear("2019-01-09"))