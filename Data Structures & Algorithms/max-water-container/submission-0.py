class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        result=0
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            if result<area:
                result=area
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            
            
            
        return result
heights = [1,7,2,5,4,7,3,6]
sol=Solution()
print(sol.maxArea(heights))      