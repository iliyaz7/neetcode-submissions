class Solution:
    def trap(self, height: list[int]) -> int:
      left=0
      right=len(height)-1
      maxleft=0
      maxright=0
      water=0
      while left<right:
        if maxleft<height[left]:
          maxleft=height[left]
        if maxright<height[right]:
          maxright=height[right]
        
        if maxleft<=maxright:
          water+=maxleft-height[left]
          left+=1
        else:
          water+=maxright-height[right]
          right-=1
      return water
height = [0,2,0,3,1,0,1,3,2,1]     
sol=Solution()
print(sol.trap(height))