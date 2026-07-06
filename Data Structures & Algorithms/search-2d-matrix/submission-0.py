class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=(rows*cols)-1
        while left<=right:
            mid=left+(right-left)//2
            current_col=mid%len(matrix[0])
            current_row=mid//len(matrix[0])
            
            if matrix[current_row][current_col]==target:
                return True
            elif matrix[current_row][current_col]>target:
                right=mid-1
            else:
                
                left=mid+1
        return False
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10    
sol=Solution()
print(sol.searchMatrix(matrix,target))