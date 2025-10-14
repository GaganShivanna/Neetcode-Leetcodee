class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [ [0 for i in range(len(text2) + 1)] 
                    for j in range(len(text1) + 1)]

        for i in range(1,len(text1) + 1): 
            for j in range(1,len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                   arr[i][j] = 1 + arr[i - 1][j - 1]

                else:
                    arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
        return arr[i][j]
                
                