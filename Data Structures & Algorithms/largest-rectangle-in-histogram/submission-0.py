class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
      stack=[]
      max_area=0
      for i in range(len(heights)):
        while stack and heights[i]<heights[stack[-1]]:
          height=heights[stack.pop()]
          right=i-1
          if len(stack)==0:
            left=0
          else:
            left=stack[-1]+1
          width=right-left+1
          area=height*width
          max_area=max(area,max_area)
        stack.append(i)
      while stack:
        height=heights[stack.pop()]
        if len(stack)==0:
          left=0
        else:
          left=stack[-1]+1
        right=len(heights)-1
        width=right-left+1
        area=height*width
        max_area=max(area,max_area)
      return max_area
heights = [2,2]
sol=Solution()
print(sol.largestRectangleArea(heights))