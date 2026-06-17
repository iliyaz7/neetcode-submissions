from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        for _ in range(len(s)):
            if i >= len(s):
                break

            
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)

            i = j + 1 + length

        return decoded