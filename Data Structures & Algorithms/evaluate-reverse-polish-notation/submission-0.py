
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
      stack=[]
      symbol=["+","-","*","/"]
      for ch in tokens:
        if ch not in symbol:
          stack.append(int(ch))
        elif ch in symbol:
          #Just remember:First pop = right operand,Second pop = left operand
          right=stack.pop()
          left=stack.pop()
          if ch=="+":
            stack.append(left+right)
          elif ch=="-":
              stack.append(left-right)
          elif ch=="*":
            stack.append(left*right)
          else:
              stack.append(int(left/right))
      return stack[-1]
tokens = ["1","2","+","3","*","4","-"]
sol=Solution()
print(sol.evalRPN(tokens))      