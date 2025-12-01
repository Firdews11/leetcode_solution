1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float('inf')
4        max_profit = 0
5        for price in prices:
6            if price < min_price:
7                min_price = price
8
9            profit = price - min_price
10
11            if profit > max_profit:
12                max_profit = profit
13                
14        return max_profit