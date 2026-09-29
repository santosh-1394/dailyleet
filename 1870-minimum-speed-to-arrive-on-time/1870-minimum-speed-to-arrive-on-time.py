class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)
        
        
        def can_arrive(speed):
            time = 0.0
            for i in range(n - 1):
                
                time += (dist[i] + speed - 1) // speed
            
            time += dist[-1] * 1.0 / speed
            return time <= hour
        
        left, right = 1, 10**7
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_arrive(mid):
                result = mid
                right = mid - 1 
            else:
                left = mid + 1  
        
        return result
