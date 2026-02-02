class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = 51 
        b = 51 
        for i in range(1, len(nums)):
            if nums[i] < a:
                b= a 
                a= nums[i]
            elif nums[i] < b: 
                b= nums[i]
            if a == 1 and b == 1:
                break
        return nums[0] + a + b