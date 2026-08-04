class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        j=n
        if j == 1 :
            return True
        
        if j % 2 != 0  or j <= 0 :
            return False
        else :
            return self.isPowerOfTwo(int(n//2)) 

         
    
        