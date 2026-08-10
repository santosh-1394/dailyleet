class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        player_colors = [{} for _ in range(n)]
        
        for x, y in pick:
            if y not in player_colors[x]:
                player_colors[x][y] = 0
            player_colors[x][y] += 1
        
        winners = 0
        
        for i in range(n):
            for color in player_colors[i]:
                if player_colors[i][color] >= i + 1:  
                    winners += 1
                    break  
        
        return winners
