class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left,right = max(weights), sum(weights)
        res = right
        def canShip(cap):
            ships, currentcap = 1, cap

            for w in weights:
                if currentcap - w < 0 :
                    ships+=1
                    currentcap = cap
                currentcap-=w
            return ships <= days
        

        while left <= right:
            cap = (left + right) // 2

            if canShip(cap):
                res = min(res, cap)
                right = cap - 1
            else:
                left = cap + 1

        return res
                




        