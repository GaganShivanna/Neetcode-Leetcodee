class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subMax = nums[0]
        curSum = 0 

        for n in nums: 
            if curSum < 0:
                curSum = 0 
            curSum += n
            subMax = max(subMax, curSum)
        return subMax