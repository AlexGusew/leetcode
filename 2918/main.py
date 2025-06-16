class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        s1 = sum(i or 1 for i in nums1)
        s2 = sum(i or 1 for i in nums2)
        if s1 < s2:
            s1, s2 = s2, s1
        :wa

"""
Input: nums1 = 
[3,2,0,1,0], nums2 = 
6, 2
[6,5,0]
ķ11,
j
r

10 1 <-- bigger sum
3 1

10 0
3 1 <-- z2 bigger than sum1, return sum1

10 1
3 0 <-- return -1

10 0
3 0 <-- return -1

3 0
3 0 <-- return  val
"""
