class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        records = set()
        for num in nums:
            if num in records:
                return True 
            records.add(num)
        return False