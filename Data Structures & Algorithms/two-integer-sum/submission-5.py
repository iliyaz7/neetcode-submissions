class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i,num in enumerate(nums):
            need=target-num
            if need in track:
                return [track[need],i]
            track[num]=i
            


nums=[3,4,5,6]
target=7
sol=Solution()
print(sol.twoSum(nums,target))