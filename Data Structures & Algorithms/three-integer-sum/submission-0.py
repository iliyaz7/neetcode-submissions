class Solution:  
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums2=sorted(nums)
    result=[]
    for i in range(len(nums)-2):

      if i>0:
        if nums2[i]==nums2[i-1]:
          continue
      left=i+1
      right=len(nums2)-1
      
      while left<right:
        total=nums2[i]+nums2[left]+nums2[right]
        if total==0:
          result.append([nums2[i],nums2[left],nums2[right]])
          left+=1
          right-=1
        
          while left<right and nums2[left]==nums2[left-1]:
            left+=1
          
          while left<right and nums2[right]==nums2[right+1]:
           right-=1
          
        elif total>0:
          right-=1
        else:
          left+=1          
    return result  
nums = [-2,0,0,2,2]
sol=Solution()
print(sol.threeSum(nums))
