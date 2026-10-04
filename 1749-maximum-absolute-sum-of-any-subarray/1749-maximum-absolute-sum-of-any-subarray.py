class Solution(object):
    def maxAbsoluteSum(self, nums):
        current_max = max_sum = 0
        current_min = min_sum = 0

        for num in nums:
            current_max = max(0, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(0, current_min + num)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))