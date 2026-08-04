class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        j = n
        if j == 1 :
            return True 
        elif j % 4 !=0 or j <= 0 :
            return False 
        else :
            return self.isPowerOfFour(int(j//4))