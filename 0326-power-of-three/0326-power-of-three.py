class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        j=n
        if j == 1 :
            return True
        
        if j % 3 != 0  or j <= 0 :
            return False
        else :
            return self.isPowerOfThree(int(n//3)) 