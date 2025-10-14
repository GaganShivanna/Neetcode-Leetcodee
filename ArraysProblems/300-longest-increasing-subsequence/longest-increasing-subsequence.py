class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums2 = []
        nums2 = sorted(set(nums))
        arr = [[0 for i in range(len(nums) + 1)] 
                for j in range(len(nums2) + 1)]
                
        for i in range(1, len(nums2) + 1): 
            for j in range(1, len(nums) + 1):
                if nums2[i - 1] == nums[j - 1]:
                    arr[i][j] = 1 + arr[i - 1][j - 1]
                else:
                    arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
        return arr[len(nums2)][len(nums)]

                