class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        length = 1
        while length < k:
            length *= 2

        shifts = 0

        while k > 1:
            half = length // 2
            if k > half:
                k -= half
                shifts += 1
            length = half

        
        return chr(ord('a') + shifts % 26)

