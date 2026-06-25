class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      left=0
      best=0
      freq={}
      for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        most_freq=max(freq.values())
        while (right-left+1)-most_freq>k:
          freq[s[left]]-=1
          left+=1
        best=max(best,right-left+1)
      return best
          
s = "XYYX" 
k=2
sol=Solution()
print(sol.characterReplacement(s,k))       