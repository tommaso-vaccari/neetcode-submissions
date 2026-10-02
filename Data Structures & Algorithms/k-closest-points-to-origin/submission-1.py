import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #UMPIRE
        # Another solution but keeping only at maximum k element in the 
        # heap. To do that i can use a max heap. If push in it if i have less than k element
        # otherwise i have to check if the new element is farthes than the farthes one, 
        # if not i pop the farthes one and push the new one and so on. 
        # When i have finished i can return that points
        # i need to use the negated distance
        # head of the max heap -3, if i receive -5 , which is greater than the current max dist
        # i throw it away, otherwise for example -2 i can keep it and push away the most 
        # distant for now
        temp = list()
        for i in range(len(points)):
            x = points[i][0]
            y = points [i] [1]
            dist = x**2 + y**2
            if len(temp) < k:
                heapq.heappush(temp,[-dist, i])
            elif (-temp[0][0] > dist) :
                # i need to insert it 
                #pop and push
                heapq.heappop(temp)
                heapq.heappush(temp, [-dist, i])
        
        # now in temp i have the points
        res = list()

        for m in temp:
            index = m[1]
            res.append(points[index])
        return res
            

            

            

        