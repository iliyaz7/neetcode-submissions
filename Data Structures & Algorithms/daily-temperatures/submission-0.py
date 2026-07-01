class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
      answer=[0]*len(temperatures)
      stack=[]
      
      for current_idx in range(len(temperatures)):
        if len(stack)==0:
          stack.append(current_idx)
          continue
    
        while stack and temperatures[current_idx]>temperatures[stack[-1]]:
          pop_idx=stack.pop()
          answer[pop_idx]=current_idx-pop_idx
        stack.append(current_idx)
      return answer
temperatures = [30,38,30,36,35,40,28]
sol=Solution()
print(sol.dailyTemperatures(temperatures))