class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output= [] 
        for i in range(2):
            for n in nums:
                output.append(n)
        return output