'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:
nums1.length == m
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr= nums1 + nums2
        arr.sort()
        if len(arr) == 1:
            return (arr[0])
        else:
            if (len(arr))%2 == 0:
                median = arr[((len(arr))//2)-1] + arr[((len(arr))//2+1)-1]
                median = float(median/2.0)
            else :
                median = arr[((len(arr)+1)//2)-1]
            return(median)

solution = Solution()
print(solution.findMedianSortedArrays([4,6,9,1], [1,8,0,2,3,5,7]))