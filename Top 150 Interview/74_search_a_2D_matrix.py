

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])
        row=len(matrix)
        
        l,r=0,row-1
        
        def search(mid):
            l,r=0,col-1
            while l<=r:
                m=(l+r)//2
                if matrix[mid][m]==target:
                    return True
            
                if target<matrix[mid][m]:
                    r=m-1
                else:
                    l=m+1
                    
            return False
        
        
        
        while l<=r:
            mid=(l+r)//2
            
            
            if matrix[mid][0]<=target<=matrix[mid][col-1]:
                return search(mid)
                    
            if target<matrix[mid][col-1]:
                r=mid-1
            else:
                l=mid+1
                
        return False
            
            
        