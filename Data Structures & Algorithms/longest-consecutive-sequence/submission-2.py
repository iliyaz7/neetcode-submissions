class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        sorted_nums=sorted(nums)
        max_length=1
        current_length=1
        for i in range(1,len(nums)):
            if sorted_nums[i]==sorted_nums[i-1]:
                continue
            if sorted_nums[i]-1==sorted_nums[i-1]:
                current_length+=1
            else:
                current_length=1
            max_length=max(current_length,max_length)
        return max_length
nums=[2,20,4,10,3,4,5]
sol=Solution()
print(sol.longestConsecutive(nums))

