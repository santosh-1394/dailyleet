class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        result = right

        while left <= right:
            mid = (left + right) // 2
            needed_days = 1
            current_load = 0

            for w in weights:
                if current_load + w > mid:
                    needed_days += 1
                    current_load = 0
                current_load += w

            if needed_days <= days:
                result = mid
                right = mid - 1  
            else:
                left = mid + 1  

        return result
