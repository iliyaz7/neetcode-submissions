class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track={}
        for value in strs:
            key="".join(sorted(value))
            if key not in track:
                track[key]=[]
            track[key].append(value)
        return list(track.values())
strs=["act","pots","tops","cat","stop","hat"]
sol=Solution()
print(sol.groupAnagrams(strs))