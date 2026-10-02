import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Two possible approaches
        # Sorting the array O(nlogn + linear scan in the worst case)
        # Heapq with negated values O(n + k*log(n))
        negated_nums = [-x for x in nums]
        heapq.heapify(negated_nums)

        # K is for sure less or equal than the length of the array so it's safe
        # to pop until k

        j = 0
        while True:
            j+=1
            if k== j:
                return -heapq.heappop(negated_nums)
            heapq.heappop(negated_nums)
        
            
        

        