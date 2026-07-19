class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        remainder_count = {0: 1} 
        result = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                result += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return result
