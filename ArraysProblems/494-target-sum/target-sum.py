class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} 
        def backtrack(index, cur_sum):
            if index == len(nums):
                return 1 if cur_sum == target else 0 
            if (index, cur_sum) in dp:
                return dp[(index, cur_sum)]

            dp[(index, cur_sum)] = backtrack(index + 1, cur_sum + nums[index]) + backtrack(index + 1, cur_sum - nums[index])
            return dp[(index, cur_sum)]
        return backtrack(0,0)