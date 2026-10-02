import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #UMPIRE
        # I need to return the kth closest point to the origin,
        # I can use a min heap built from the list of points O(n)
        # and pop for kth time to obtain the kth closest i can store a tuple(dist**2, index)

        temp = list()

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            temp.append([x**2+ y**2,i])

        heapq.heapify(temp)
        result = list()
        for _ in range(k):
            point_index = heapq.heappop(temp)[1]
            result.append(points[point_index])

        return result
        

    


        