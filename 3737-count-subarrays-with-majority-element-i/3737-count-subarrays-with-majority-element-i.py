class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        mapped = [1 if x == target else -1 for x in nums]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + mapped[i]
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if pref[j] > pref[i]:
                    ans += 1
        return ans
