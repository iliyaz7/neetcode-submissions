class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
        return []

nums=[4,5,6]
target=10
print(Solution().twoSum(nums,target))