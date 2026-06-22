class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      low_price=prices[0]
      best_profit=0
      for right in range(1,len(prices)):
        if prices[right]<low_price:
          low_price=prices[right]
        current_profit=prices[right]-low_price
        if current_profit>best_profit:
          best_profit=current_profit
      return best_profit
        
          
prices = [10,1,5,6,7,1]
sol=Solution()
print(sol.maxProfit(prices))        