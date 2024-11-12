# 3 Sum : Find triplets that add up to a zero
"""
Example 1:
Input:
 nums = [-1,0,1,2,-1,-4]

Output:
 [[-1,-1,2],[-1,0,1]]

Explanation:
 Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

Example 2:
Input:
 nums=[-1,0,1,0]
Output:
 Output: [[-1,0,1],[-1,1,0]]
Explanation:
 Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k
 """

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, j in enumerate(nums):
            if i>0 and j == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1

            while l<r:
                sum3 = j+nums[l]+nums[r]

                if sum3>0:
                    r-=1
                elif sum3<0:
                    l+=1
                else:
                    res.append([j,nums[l],nums[r]])
                    l+=1
                    while l<r and num[l]==num[l-1]:
                        l+=1
        return res