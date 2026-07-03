class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack=[]       
        car=list()
        for i in range(len(position)):
          car.append((position[i],speed[i]))
        car.sort(reverse=True)
          
        for pos,spd in car:            
          current_time=(target-pos)/(spd)
          if len(stack)==0:
            stack.append(current_time)
          elif current_time>stack[-1]:
            stack.append(current_time)
        return len(stack)
        
          
target = 10
position = [1,4]
speed = [3,2]
sol=Solution()
print(sol.carFleet(target,position,speed))