class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sorted_num=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_num[i][0])
        return result
        
nums=[1,2,2,3,3,3]
k=2
        