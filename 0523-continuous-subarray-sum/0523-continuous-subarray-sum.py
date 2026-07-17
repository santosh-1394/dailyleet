class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sum = 0
        mod_map = {0: -1}  
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in mod_map:
                
                if i - mod_map[remainder] > 1:
                    return True
            else:
                mod_map[remainder] = i
        
        return False
