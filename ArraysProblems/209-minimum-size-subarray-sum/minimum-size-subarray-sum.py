class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 

        current_sum = 0
        l = 0 
        minsub = float('inf')
        for r in range(n):
            current_sum += nums[r]
            while current_sum >= target:
                minsub = min(minsub, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return 0 if minsub == float('inf') else minsub