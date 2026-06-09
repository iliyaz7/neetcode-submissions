class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track={}
        for i in range (len(nums)):
            track[nums[i]]=track.get(nums[i],0)+1
            sorted_items=sorted(track.items(),key=lambda x:x[1],reverse=True)
            new_track=[key for key,value in sorted_items]
            
        return list(new_track[0:k])
         

nums=[1,2,2,3,3,3]
k=2
sol=Solution()
print(sol.topKFrequent(nums,k))