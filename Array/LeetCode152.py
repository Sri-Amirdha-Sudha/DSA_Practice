class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1
        for i in nums:
            if i==0:
                curMax, curMin = 1,1
                continue
            temp = curMax*i
            curMax = max(i*curMax,i*curMin,i)
            curMin = min(temp, curMin*i, i)
            res = max(res,curMax)
        return res