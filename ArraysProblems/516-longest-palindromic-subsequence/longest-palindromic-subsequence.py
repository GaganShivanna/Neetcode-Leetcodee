class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]  # reversed string
        n = len(s)
        
        # Create DP table (LCS between s and s2)
        arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    arr[i][j] = 1 + arr[i - 1][j - 1]
                else:
                    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        
        return arr[n][n]
