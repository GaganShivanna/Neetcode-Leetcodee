class Solution:
    def maxProfit(self, price: List[int]) -> int:
        max_profit = 0 
        l, r = 0, 1

        while r < len(price):
            if price[l] < price[r]: 
                max_profit = max(max_profit, price[r] - price[l])
            else:
                l = r 
            r += 1
        return max_profit
