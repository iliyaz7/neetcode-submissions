class Solution:
    def isValid(self, s: str) -> bool:
      stack=[]
      bracket={")":"(",
               "]":"[",
               "}":"{"}
      for ch in s:
        if ch  in bracket.values():
          stack.append(ch)
        elif ch in bracket.keys():
          if len(stack)==0:
            return False
          elif bracket[ch]==stack[-1]:
            stack.pop()
          else:
            return False
      if len(stack)==0:
        return True
      else:
        return False    
s = "([{}])"
sol=Solution()
print(sol.isValid(s))