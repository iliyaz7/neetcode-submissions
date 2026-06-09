class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
nums=[1,2,3,3]
solution=Solution()
print(solution.hasDuplicate(nums))
        