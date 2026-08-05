class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """

        def solve(k):
            if k == 1:
                return 0

            length = 1
            while length < k:
                length *= 2

            half = length // 2

            if k > half:
                return solve(k - half) + 1
            else:
                return solve(k)

        shifts = solve(k)
        return chr(ord('a') + shifts % 26)