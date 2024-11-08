# Maximum Sum of Subarray
"""
Example 1:
Input:
 arr = [-2,1,-3,4,-1,2,1,-5,4] 
Output:
 6 
Explanation:
 [4,-1,2,1] has the largest sum = 6. 
Examples 2:
Input:
 arr = [1] 
Output:
 1 
Explanation:
 Array has only one element and which is giving positive sum of 1. 
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum
