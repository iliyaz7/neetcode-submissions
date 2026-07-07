import math as m
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

      left=1
      right=max(piles)
      
      while left<=right:
        mid=(left+right)//2
        total_hour=0
        for i in range(len(piles)): 
          total_hour+=m.ceil(piles[i]/mid)
        if total_hour<=h:
            
            right=mid-1
        else:
            left=mid+1
      return left      
piles= [1,4,3,2]
h = 9   
sol=Solution()
print(sol.minEatingSpeed(piles,h))